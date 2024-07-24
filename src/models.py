import os
import sys, enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class MediaType(enum.Enum):
    jpg="jpg"
    mp4="mp4"
    png="png"

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id_follower = Column(Integer, primary_key=True)
    id_from_user = Column(Integer, ForeignKey('user.id_user'))
    id_to_user = Column(Integer, ForeignKey('user.id_user'))  

class Post(Base):
    __tablename__ = 'post'
    id_post = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))

class Media(Base):
    __tablename__ = 'media'
    id_media = Column(Integer, primary_key=True)
    id_post = Column(Integer, ForeignKey('post.id_post'))
    type = Column(Enum(MediaType), nullable=False)
    url = Column(String(80), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id_comment = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('user.id_user'))
    id_post = Column(Integer, ForeignKey('post.id_post'))
    comment_text = Column(String(120), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
