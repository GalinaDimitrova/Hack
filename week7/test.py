import pythonwhois
import requests
from bs4 import BeautifulSoup


# creation_date = pythonwhois.get_whois('hackbulgaria.com', normalized=[])['creation_date']
# print(creation_date)

url = 'http://skanev.bg'
website = requests.get(url)
html_doc = website.text
soup = BeautifulSoup(html_doc)

try:

    desc1 = soup.find(
                attrs={"property": "og:description"}).get("content")

    print(desc1)
except Exception as e:
    print('fjdsjkfsk')
    desc = ""


title = soup.title.string


print(title)

#string.encode("utf-8")
# try:

#     desc = soup.find(
#                 attrs={"name": "description"}).get("content")
#     #desc.encode(encoding ='UTF-8', errors='strict')

#     print(desc)
# except Exception as e:
#     print('fjdsjkfsk')
#     desc = ""
