from urllib import parse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

class Crawler:
    def __init__(self, domain):
        self.domain = domain
        self.scanned_urls = []
        self.to_scan = []


    def is_outgoing(self, url):
        o = urlparse(url)
        if o.netloc == self.domain:
        #if '/' + self.domain in url:
            return False
        return True

    def href_to_url(self, url, href):
        return parse.urljoin(url, href)

    def scan_page(self, url):
        if url in self.scanned_urls:
            return
        print(url)
        self.scanned_urls.append(url)
        website = requests.get(url)
        html_doc = website.text
        soup = BeautifulSoup(html_doc)

        try:
            self.__save_soup(soup, url)
        except Exception as e:
            #pass
            print(e)

        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            next_page = self.href_to_url(url, href)
            # if next_page not in self.scanned_urls and not self.is_outgoing(next_page):
            #     self.scan_page(next_page)

            if not self.is_outgoing(next_page) and '#' not in next_page:
                self.to_scan.append(next_page)


    def __save_soup(self, soup, url):
        pass

    def scan_website(self):
        url = 'http://' + self.domain
        self.scan_page(url)
        while len(self.to_scan) != 0:
            self.scan_page(self.to_scan.pop())


def main():
    #crawler = Crawler("hackbulgaria.com")
    crawler = Crawler("aladinfoods.bg")
    crawler.scan_website()


if __name__ == '__main__':
    main()
