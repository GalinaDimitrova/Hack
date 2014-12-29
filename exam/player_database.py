from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    name = Column(String, primary_key=True)
    score = Column(Integer)


def add_player( name, score):
    player = Player(name, score)
    session.add(player)
    session.commit()


def main():
    engine = create_engine("sqlite:///players.db")
    # will create all tables
    Base.metadata.create_all(engine)
    session = Session(bind=engine)


if __name__ == '__main__':
    main()