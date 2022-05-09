import time
from bs4 import BeautifulSoup
import requests


def scraper(us_state) -> str:
    print('Scraping data ...')
    url = 'https://datausa.io/profile/geo/' + us_state.casefold()
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    income = soup.find('div', text='Median Household Income').parent.find(class_='stat-value').text
    return income


def txt_srvc():
    def write_to_file(content):
        print("Writing to mc-output ...")
        file = open('mc-output.txt', 'w')
        file.write(content)
        file.close()
        del_contents()

    def read_from_file():
        print("Reading from mc-input ...")
        file = open('mc-input.txt', 'r')
        return file.readline()

    def del_contents():
        print("Emptying input file ...")
        file = open('mc-input.txt', 'w')
        file.write('')
        file.close()

    while True:
        time.sleep(1)
        line = read_from_file()
        if line is not None:
            print('US State found!')
            income = scraper(line)
            write_to_file(income)


def main():
    txt_srvc()


main()
