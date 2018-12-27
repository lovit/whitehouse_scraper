from .utils import get_soup
from .utils import now

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.select('h1[class=page-header__title]')[0].text
        time = soup.select('time')[0].text
        phrases = soup.select('div[class^=page-content__content] p')
        content = '\n'.join([p.text.strip() for p in phrases])

        json_object = {
            'title' : title,
            'time' : time,
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None