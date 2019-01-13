import re
import time
from .utils import get_soup
from .utils import news_dateformat
from .utils import user_dateformat
from .utils import strf_to_datetime


def get_latest_allnews(begin_date, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns = [
    re.compile('https://www.whitehouse.gov/briefings-statements/[\w]+'),
    re.compile('https://www.whitehouse.gov/presidential-actions/[\w]+'),
    re.compile('https://www.whitehouse.gov/articles/[\w]+')]
url_base = 'https://www.whitehouse.gov/news/page/{}/'

def is_matched(url):
    for pattern in patterns:
        if pattern.match(url):
            return True
    return False

def get_allnews_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    urls_all : list of str
        List of urls
    """

    urls_all = []
    for page in range(begin_page, end_page+1):
        url = url_base.format(page)
        soup = get_soup(url)
        links = soup.select('a[href^=https://www.whitehouse.gov/]')
        urls = [link.attrs.get('href', '') for link in links]
        urls = [url for url in urls if is_matched(url)]
        urls_all += urls
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return urls_all

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number. 
        eg: 503 in 'https://www.whitehouse.gov/news/page/503'
    """

    def last_element(url):
        parts = [p for p in url.split('/') if p]
        return int(parts[-1])

    soup = get_soup('https://www.whitehouse.gov/news/')
    last_page = max(
        last_element(a.attrs['href'])
        for a in soup.select('a[class=page-numbers]')
    )

    return last_page