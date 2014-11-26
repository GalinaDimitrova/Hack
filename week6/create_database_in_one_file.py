from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DATETIME
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rate = Column(Float)


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    # Add FK
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projections")

    type = Column(String)
    date_time = Column(DATETIME)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    # Add FK
    projection_id = Column(Integer, ForeignKey("projections.id"))
    reservation = relationship("Projection", backref="reservations")

    row = Column(Integer)
    col = Column(Integer)


engine = create_engine("sqlite:///cinema.db")
# will create all tables
Base.metadata.create_all(engine)
