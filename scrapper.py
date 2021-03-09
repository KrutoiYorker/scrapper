import requests
from bs4 import BeautifulSoup
import settings

def get_movies_info_raw():
    try:
        res = requests.get(settings.movies_url)
    except Exception as e:
        raise Exception(f"Request was failed: {e}")
    if res.status_code in settings.STATUS_CODES:
        movies_html = res.text
        if movies_html:
            return movies_html
        else:
            return False