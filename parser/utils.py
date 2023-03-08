import requests
from bs4 import BeautifulSoup
import lxml


def parser(tag):
    result = []
    for page in range(1, 2):
        url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=newest&page={page}&pagesize=50'
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        question_titles = soup.find_all(
            'h3', class_='s-post-summary--content-title')
        for question_title in question_titles:
            link = question_title.find('a', href=True)['href']
            title = question_title.find('a', href=True).text.strip()
            result.append([title, f'https://stackoverflow.com{link}'])
    return result
