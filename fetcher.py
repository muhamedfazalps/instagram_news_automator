import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_articles():
    try:
        response = requests.get(BASE_URL, params={"country": "in", "category": "general", "apiKey": NEWS_API_KEY})
        return response.json().get("articles", [])
    except:
        return []

def fetch_all_headlines(limit=5):
    return [a["title"] for a in fetch_articles()[:limit]]
