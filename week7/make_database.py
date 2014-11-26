from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DATETIME, Boolean
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class Website(Base):
    __tablename__ = "website"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    time = Column(DATETIME)
    HTML5 = Column(Boolean)
    ssl = Column(Boolean)


class Page(Base):
    __tablename__ = "page"
    id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey("website.id"))
    movie = relationship("Website", backref="page")
    title = Column(String)
    description = Column(String)
    url = Column(String)
    dirty_words = Column(Boolean)


engine = create_engine("sqlite:///search-engine.db")
# will create all tables
Base.metadata.create_all(engine)