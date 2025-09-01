from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

base = declarative_base()
engine = create_engine("sqlite:///dino.db")
session = sessionmaker(bind=engine)

