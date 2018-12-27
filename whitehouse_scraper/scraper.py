import re
import time
from .utils import get_soup

def get_latest_allnews(last_date, sleep=1.0):
    """
    Artuments
    ---------
    last_date : Date
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns = [
    re.compile('https://www.whitehouse.gov/briefings-statements/[\w]+'),
    re.compile('https://www.whitehouse.gov/presidential-actions/[\w]+'),
    re.compile('https://www.whitehouse.gov/articles/[\w]+')]
url_base = 'https://www.whitehouse.gov/news/page/{}/'

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
    links_all : list of str
        List of urls
    """

    def is_matched(url):
        for pattern in patterns:
            if pattern.match(url):
                return True
        return False

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_base.format(page)
        soup = get_soup(url)
        links = soup.select('a[href^=https://www.whitehouse.gov/]')
        links = [link.attrs.get('href', '') for link in links]
        links = [link for link in links if is_matched(link)]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return links_all

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number. 
        eg: 503 in 'https://www.whitehouse.gov/news/page/503'
    """
    raise NotImplemented