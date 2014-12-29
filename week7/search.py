from make_database import Page, Website
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


engine = create_engine("sqlite:///storage.db")
session = Session(bind=engine)

search_word = input("What you want to search: ")
results = session.query(Page.title, Page.description, Page.url).all()

answer = []


def word_in_title(result):
    if result.title and search_word in result.title:
        return True
    return False


def word_in_desc(result):
    if result.description and search_word in result.description:
        return True
    return False


def word_in_url(result):
    if result.url and search_word in result.url:
        return True
    return False

for result in results:

    if word_in_title(result) and word_in_desc(result) and word_in_url(result):
        answer.append(result.url)
    elif word_in_title(result) and word_in_desc(result):
        answer.append(result.url)
    elif word_in_title(result):
        answer.append(result.url)

if answer == []:
    print("Nothing found!")
for ans in answer:
    print(ans)
