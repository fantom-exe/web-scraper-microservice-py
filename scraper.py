import time
from bs4 import BeautifulSoup
import requests


def scraper(us_state) -> str:
    url = 'https://datausa.io/profile/geo/' + us_state.casefold()
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    income = soup.find('div', text='Median Household Income').parent.find(class_='stat-value').text
    return income


def txt_srvc():
    def write_to_file(content):
        print("Writing to file ...")
        file = open('mc-output.txt', 'w')
        file.write(str(content))
        file.close()

    def read_from_file():
        print("Reading from file ...")
        file = open('mc-input.txt', 'r')
        return file.readline()

    while True:
        time.sleep(2)
        line = read_from_file()
        if line not None:
            income = scraper(line)
            write_to_file()


def main():
    txt_srvc()
    print()


main()
