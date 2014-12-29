from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = declarative_base()


class PlayerDB(Base):
    __tablename__ = "player"
    username = Column(String, primary_key=True)
    score = Column(Integer, default=0)

engine = create_engine("sqlite:///player.db")
Base.metadata.create_all(engine)



class Player():

    def __init__(self, playername, score):
        self.session = Session(bind=engine)

        self.playername = playername
        self.score = score

    def add_player(self, playername, score):
        new_player = PlayerDB(
            username=playername,
            score=score
        )
        self._session.add(new_player)
        self._session.commit()

    def update_score():
        pass

    def delete_user():
        pass

    def highscore():
        pass

