
from sqlalchemy import Column, Integer, String, Float

from connection import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rate = Column(Float)

