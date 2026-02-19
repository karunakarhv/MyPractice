import requests
from format_article import format_article_email
from send_email import send_email
from dotenv import load_dotenv
import os

def fetch_news(api_key, query, language='en', country=None, category=None):
    url = 'https://newsdata.io/api/1/news'
    params = {
        'apikey': api_key,
        'q': query,
        'language': language
    }
    if country:
        params['country'] = country
    if category:
        params['category'] = category

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    to_email = os.getenv('TO_EMAIL')

    topics = {
        'cricket': 'Latest Cricket News',
        'politics': 'Latest Political Updates',
        'finance': 'Latest Financial News',
        'sports': 'Latest Sports Headlines'
    }

    for query, subject in topics.items():
        news_data = fetch_news(API_KEY, query)
        body = format_article_email(news_data)
        send_email(
            subject,
            body,
            to_email
        )