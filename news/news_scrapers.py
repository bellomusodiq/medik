from .models import Article
import requests
from bs4 import BeautifulSoup
from medik.scheduler import scheduler


def parse_havard():
    url = 'https://www.health.harvard.edu/blog/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    news = soup.find_all('div', class_="post-wrapper")
    Article.objects.all().delete()
    for article in news:
        title = article.find('h2', class_='entry-title').find('a').text
        url = article.find('h2', class_='entry-title').find('a')['href']
        summary = article.find('section', class_='entry-summary').find("p").text
        Article.objects.create(
            title=title,
            url=url,
            description=summary
        )


def parse_healthline():
    url = 'https://www.healthline.com/nutrition'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    news = soup.find_all(class_='css-18vzruc')
    for article in news:
        title = article.find(class_="css-1ey785u").text
        url = 'https://www.healthline.com' + article.find(class_="css-1axlply")["href"]
        summary = article.find(class_="css-2fdibo").text
        Article.objects.create(
            title=title,
            url=url,
            description=summary
        )


def parse():
    Article.objects.all().delete()
    parse_havard()
    parse_healthline()


scheduler.remove_all_jobs()
scheduler.add_job(parse, 'interval', minutes=60)
