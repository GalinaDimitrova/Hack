import requests
from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import urlparse
from make_database import Base
from make_database import Page, Website
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pythonwhois


class Crawler:

    def __init__(self, domain, domain_id, session):
        self.scanned_urls = []
        self.domain = domain
        self._domain_id = domain_id
        self._session = Session(bind=session)
        self.to_scan = []

    def is_outgoing(self, url):
        obj = urlparse(url)
        if obj.netloc == self.domain and '#' not in url and 'share' not in url:
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
            self.save_page_in_DB(soup, url)
        except Exception as e:
            print(e)

        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            next_page = self.href_to_url(url, href)
            if next_page not in self.scanned_urls and not self.is_outgoing(
                    next_page):
                self.to_scan.append(next_page)

    def save_page_in_DB(self, soup, url):
        try:
            desc = soup.find(
                attrs={"property": "og:description"}).get("content")
            print(desc)
        except Exception as e:
            print('No description!')
            desc = ""

        new_page = Page(
            website_id=self._domain_id,
            title=soup.title.string,
            description=desc,
            url=url
        )

        self._session.add(new_page)
        self._session.commit()

    def scan_website(self):
        url = 'http://' + self.domain
        self.scan_page(url)
        while len(self.to_scan) != 0:
            self.scan_page(self.to_scan.pop())


def save_website_in_DB(url, session):
    my_session = Session(bind=session)
    new_site = Website(
        url=url
        #time_activated = creation_date
    )

    my_session.add(new_site)
    my_session.commit()

    my_domain_id = my_session.query(
        Website.id).filter(Website.url == url).all()
    return my_domain_id


def main():
    #crawler = Crawler("hackbulgaria.com")
    # crawler = Crawler("xmlcourse.hit.bg")
    # crawler = Crawler("skanev.com")
    #crawler = Crawler("aladinfoods.bg")
    #crawler.scan_website()

    url = "hackbulgaria.com"
    engine = create_engine("sqlite:///storage.db")
    Base.metadata.create_all(engine)

    # creation_date = pythonwhois.get_whois(url, normalized=[])['creation_date']
    # print(creation_date)

    my_domain_id = save_website_in_DB("http://{}".format(url), engine)
    crawler = Crawler(url, my_domain_id[0][0], engine)
    crawler.scan_website()

if __name__ == '__main__':
    main()
