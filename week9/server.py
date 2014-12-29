from flask import Flask
from flask import request
from flask import render_template
from local_settings import debug_mode

from make_database import Page, Website
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import or_


app = Flask(__name__)


@app.route('/')
def index():
    html = open('index.html', 'r').read()
    return html


def word_in_title(search_word, result):
    if result.title and search_word in result.title:
        return True
    return False


def word_in_desc(search_word, result):
    if result.description and search_word in result.description:
        return True
    return False


def word_in_url(search_word, result):
    if result.url and search_word in result.url:
        return True
    return False


@app.route('/search/')
def search():

    engine = create_engine("sqlite:///storage.db")
    session = Session(bind=engine)
    key_word = request.args.get('key_words', '')

    pages = session.query(Page).filter(or_(Page.title.like(
        '%' + key_word + '%'), Page.description.like(
        '%' + key_word + '%'), Page.url.like('%' + key_word + '%')))

    # result = []

    # pages = session.query(Page.title, Page.description, Page.url).all()

    # for page in pages:
    #     if word_in_title(key_word, page) and word_in_desc(key_word, page) and word_in_url(key_word, page):
    #         result.append(page)
    #     elif word_in_title(key_word, page) and word_in_desc(key_word, page):
    #         result.append(page)
    #     elif word_in_title(key_word, page):
    #         result.append(page)

    # return render_template('result.html', pages=result)

    return render_template('result.html', pages=pages)


if __name__ == '__main__':
    app.run(debug=debug_mode)



# self.cursor.execute(
#   "select string from stringtable where string like ? and type = ?",
#   ('%'+searchstr+'%', type))