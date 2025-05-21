from django.shortcuts import render
import requests
from django.conf import settings
from django.utils.html import mark_safe
import markdown

# Create your views here.

Gemini_API_KEY =settings.GOOGLE_GENAI_API_KEY

API_KEY = settings.PROGRAMMABLE_SEARCH_ENGINE_API_KEY
CX = settings.PROGRAMMABLE_SEARCH_ENGINE_CX


def index(request):
    pexels_api_key = settings.PEXELS_API_KEY
    return render(request, 'core/index.html',{
        'pexels_api_key': pexels_api_key,
    })


def search_page(request):
    tabs = ['web', 'images', 'videos', 'news', 'maps', 'books', 'shorts', 'finance', 'forums']
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'web')  # default to 'web'
    page = int(request.GET.get('page', 1))
    start_index = (page - 1) * 10 + 1
    category = request.GET.get('category', '')

    results = []
    total_results = 0
    ai_overview = ""

    if query:
        # Add search type to query to filter it
        refined_query = f"{query} site:{search_type}" if search_type != 'web' else query

        params = {
            'key': API_KEY,
            'cx': CX,
            'q': refined_query,
            'start': start_index,
        }
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        data = response.json()

        results = data.get('items', [])
        total_results = int(data.get('searchInformation', {}).get('totalResults', 0))
        ai_overview = ""
        if results and page == 1:
            # Generate a simple summary using the first 3 result snippets as context for the AI
            snippets = " ".join([result.get('snippet', '') for result in results[:3]]) if results else ""
            if snippets:
                # Check if the displayLink values are different
                display_links = {result.get('displayLink', '') for result in results[:3]}
                if len(display_links) > 1:
                    ai_prompt = (
                        f"Compare the following search results for the query '{query}'. "
                        f"Combine and compare their content based on their sources. Make bold or add emphasis on key areas. "
                        + "\n\n".join(
                            f"Source: {result.get('displayLink', '')}\nSnippet: {result.get('snippet', '')}"
                            for result in results[:3]
                        )
                    )
                else:
                    ai_prompt = (
                        f"Summarize the following search result into a brief overview for the query '{query}': {snippets}"
                    )
                try:
                    gemini_response = requests.post(
                        'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
                        params={'key': Gemini_API_KEY},
                        json={
                            'contents': [
                                {'parts': [{'text': ai_prompt}]}
                            ],
                            'generationConfig': {
                                'maxOutputTokens': 150  # Limit response length
                            }
                        },
                        timeout=10
                    )
                    if gemini_response.status_code == 200:
                        response_data = gemini_response.json()
                        ai_overview_markdown = (
                            response_data.get('candidates', [{}])[0]
                            .get('content', {})
                            .get('parts', [{}])[0]
                            .get('text', '')
                        )
                        # Convert markdown to HTML and mark as safe for template rendering
                        ai_overview = mark_safe(markdown.markdown(ai_overview_markdown))
                        if not ai_overview:
                            print("AI overview is empty. Response data:", response_data)
                            ai_overview = "AI overview could not be generated."
                    else:
                        print("Gemini API error:", gemini_response.status_code, gemini_response.text)
                        ai_overview = "AI overview could not be generated."
                except Exception as e:
                    print("Exception during Gemini API call:", str(e))
                    ai_overview = "AI overview could not be generated."
            else:
                ai_overview = "No overview available."
            

            

    return render(request, 'core/search.html', {
        'tabs': tabs,
        'results': results,
        'query': query,
        'ai_overview': ai_overview,
        'category': category,
        'type': search_type,
        'page': page,
        'start_index': start_index,
        'shown_count': start_index + len(results) - 1,
        'has_next': start_index + 10 <= total_results,
        'has_prev': page > 1,
        'total_results': total_results,
    })


   


# search images
def search_images(request):
    tabs = ['web', 'images', 'videos', 'news', 'maps', 'books', 'shorts', 'finance', 'forums']
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    start_index = (page - 1) * 10 + 1

    results = []
    total_results = 0

    if query:
        params = {
            'key': API_KEY,
            'cx': CX,
            'q': query,
            'searchType': 'image',
            'start': start_index,
            'num': 10,
        }
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get('items', [])
            total_results = int(data.get('searchInformation', {}).get('totalResults', 0))



    context = {
        'tabs': tabs,
        'results': results,
        'query': query,
        'type': 'images',
        'page': page,
        'start_index': start_index,
        'shown_count': start_index + len(results) - 1,
        'has_next': start_index + 10 <= total_results,
        'has_prev': page > 1,
        'total_results': total_results,
    }
    
    return render(request, 'core/images.html', context)



# render web_portfolio.html
def web_portfolio(request):
    return render(request, 'core/web_portfolio.html')


# ai overview

