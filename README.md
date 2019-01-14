## Usage

Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2019-01-10 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 100 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

```
python scraping_latest_news.py
```

```
[1 / 100] (January 12, 2019) Remarks by President Trump During Roundtable Discussion with State, Local, and Community Leaders on Border Security and Safe Communities
[2 / 100] (January 11, 2019) President Donald J. Trump Announces Intent to Nominate Individuals to Key Administration Posts
[3 / 100] (January 11, 2019) Statement from National Security Advisor Ambassador John Bolton on Venezuela
[4 / 100] (January 11, 2019) Remarks by Vice President Pence Before Meet-and-Greet with U.S. Customs and Border Patrol Employees
[5 / 100] (January 11, 2019) Remarks by President Trump During Briefing at the Rio Grande Valley U.S.-Mexico Border
[6 / 100] (January 11, 2019) Remarks by President Trump in Roundtable on Border Security | McAllen, TX
[7 / 100] (January 11, 2019) White House National Security Advisor Announces Senior Staff Appointment
[8 / 100] (January 10, 2019) Bill Announcement
[9 / 100] (January 10, 2019) The Crisis at the Southern Border Is Too Urgent to Ignore
[10 / 100] (January 10, 2019) Remarks by President Trump Before Marine One Departure
[11 / 100] (January 10, 2019) Secretary Nielsen: “We Face a Humanitarian and Security Crisis”
Stop scrapping. 11 / 100 news was scrapped
The oldest news has been created after 2019-01-10
```

Get news urls from specific pages

```python
from whitehouse_scraper import parse_page
from whitehouse_scraper import get_allnews_urls

urls = get_allnews_urls(begin_page=1, end_page=3, verbose=True)
for url in urls[:3]:
    json_object = parse_page(url)    
```