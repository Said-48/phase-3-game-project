from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

base = declarative_base()
engine = create_engine("sqlite:///dino.db")
session = sessionmaker(bind=engine)

class Player(base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    sessions = relationship("GameSession", backref="player")

class GameSession(base):
    __tablename__ = "game_session"
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    score = Column(Integer)