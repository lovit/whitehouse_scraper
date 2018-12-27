import re
from .utils import get_soup

def get_briefings_statements(begin_page=1, end_page=3, verbose=True):
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

    url_base = 'https://www.whitehouse.gov/news/page/{}/'
    url_pattern = re.compile('https://www.whitehouse.gov/briefings-statements/[\w]+')

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_base.format(page)
        soup = get_soup(url)
        links = soup.select('a[href^=https://www.whitehouse.gov/briefings-statements/]')
        links = [link.attrs.get('href', '') for link in links]
        links = [link for link in links if url_pattern.match(link)]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return links_all