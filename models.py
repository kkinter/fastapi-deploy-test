from database import Base
from sqlalchemy import Column, Date, Integer, String


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    artist = Column(String(128), nullable=False)
    release_date = Column(Date, nullable=False)
