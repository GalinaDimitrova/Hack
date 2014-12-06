from connection import Base, engine
from movie_ORM import Movie
from projection_ORM import Projection
from reservation_ORM import Reservation
from sqlalchemy.orm import Session

def add_movie():
    

def main():
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

if __name__ == '__main__':
    main()
