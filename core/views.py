from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.


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

   
    return render(request, 'core/search.html', {
        'tabs': tabs,
        'results': results,
        'query': query,
        'category': category,
        'type': search_type,
        'page': page,
        'start_index': start_index,
        'shown_count': start_index + len(results) - 1,
        'has_next': start_index + 10 <= total_results,
        'has_prev': page > 1,
        'total_results': total_results,
    })



# render web_portfolio.html
def web_portfolio(request):
    return render(request, 'core/web_portfolio.html')

