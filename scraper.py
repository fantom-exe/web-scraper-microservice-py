import time
from bs4 import BeautifulSoup
import requests


def scraper(us_state) -> str:
    # if State name contains space, replace with '-'
    us_state = us_state.replace(' ', '-').lower()

    print('Scraping data ...')
    url = 'https://datausa.io/profile/geo/' + us_state
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    income = soup.find('div', text='Median Household Income').parent.find(class_='stat-value').text
    return income


class textServices():
    def write_to_file(self, content):
        print("Writing to mc-output ...")
        file = open('mc-output.txt', 'w')
        file.write(content)
        file.close()
        self.del_contents('mc-input.txt')

    def read_from_file(self):
        print("Reading from mc-input ...")
        file = open('mc-input.txt', 'r')
        return file.readline()

    def del_contents(self, filename):
        print('Emptying ' + filename + ' ...')
        file = open(filename, 'w')
        file.write('')
        file.close()


def main():
    txt_srvc = textServices()
    txt_srvc.del_contents('mc-output.txt')
    txt_srvc.del_contents('mc-input.txt')

    while True:
        time.sleep(1.5)
        line = txt_srvc.read_from_file()
        if line != '':
            print('US State found!')
            income = scraper(line)
            txt_srvc.write_to_file(income)


main()
