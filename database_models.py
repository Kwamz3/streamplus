from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Movie_List(Base):
    __tablename__ = "movie_list"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(DateTime, index=True)
    runtime = Column(Integer)
    genre = Column(String, index=True)
    producer = Column(String, index=True)
    poster = Column(String)