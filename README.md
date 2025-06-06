# 🔍 Astra Search Engine

A Google-style search interface built with **Python Django**, **HTML/CSS**, and **Bootstrap**, integrated with the **Google Programmable Search Engine API**. It also features toggle tabs to showcase **AstraSoftwares' products** like Web Design, AI Systems, and SEO.

## 🌐 Features

* 🔎 Web-wide search using Google Custom Search API
* 🖼️ Image tab with full image results
* 📰 News, Videos, Books, Finance, Forums, and Maps tabs (custom UI routing)
* 🎛️ Toggle interface for AstraSoftwares products
* 📄 Pagination-ready search results
* 🧪 Clean, responsive UI with Bootstrap
* 🔐 Credentials stored in `.env` for security

## 📸 UI Preview

![UI Screenshot](screenshots/preview.png)

## 🚀 Technologies Used

* Python 3.x
* Django 4.x
* Bootstrap 5
* Google Programmable Search API
* dotenv for environment variables

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/astra-search.git
cd astra-search
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_cse_id_here
DEBUG=True
```

### 5. Run the server

```bash
python manage.py runserver
```

Then go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 How to Get Your Google API Key and CSE ID

### Step 1: Get an API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Navigate to **APIs & Services > Credentials**
4. Click **Create Credentials** > **API Key**
5. Copy the generated key and paste it into your `.env` file as `GOOGLE_API_KEY`

### Step 2: Set Up Programmable Search Engine (CSE)

1. Visit [https://programmablesearchengine.google.com/](https://programmablesearchengine.google.com/)
2. Click **Add** and follow the steps to create a new search engine
3. Under **Control Panel**, copy your **Search Engine ID** (CSE ID)
4. Paste it into your `.env` file as `GOOGLE_CSE_ID`
5. (Optional) Under **Basics > Search the entire web**, enable this option to allow global results

---

## 📁 Folder Structure

```
astra-search/
│
├── core/
│   ├── templates/core/
│   │   ├── base_search.html
│   │   ├── web.html
│   │   ├── images.html
│   │   └── ...
│   ├── views.py
│   └── urls.py
│
├── .env
├── requirements.txt
├── manage.py
└── README.md
```

---

## ✨ Future Improvements

* Add real-time suggestions (like Google Autocomplete)
* Infinite scroll or advanced pagination
* AI-powered search assistant (Gemini/ChatGPT-style)
* Dark mode toggle
* Upload as a SaaS tool with user analytics

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📞 Contact

**Developer:** Ishmael Bett
**Company:** [Astra Softwares](https://www.astrasoft.tech)
**Email:** [info.astrasoft@gmail.com](mailto:info.astrasoft@gmail.com)
**WhatsApp:** +2547 2740 5667

---

## 📜 License

MIT License © 2025 Ishmael Bett / Astra Softwares
