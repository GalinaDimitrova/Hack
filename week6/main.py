from connection import Base, engine
from movie_ORM import Movie
from projection_ORM import Projection
from reservation_ORM import Reservation
from sqlalchemy.orm import Session



def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
