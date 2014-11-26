
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from connection import Base
# A class that maps to a table, inherits from Base


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    # Add FK
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projections")

    type = Column(String)
    date_time = Column(DATETIME)

