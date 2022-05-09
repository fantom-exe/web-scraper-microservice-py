from bs4 import BeautifulSoup
import requests


def scraper(us_state):
    url = 'https://datausa.io/profile/geo/' + us_state.casefold()
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    income = soup.find('div', text='Median Household Income').parent.find(class_='stat-value').text
    return income


def main():
    income = scraper('California')
