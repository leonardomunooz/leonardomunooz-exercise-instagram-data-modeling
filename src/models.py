import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum,Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class GenderEnum(enum.Enum):
    female = "Female"
    male = "Male"
    other = "Others"
class MediaEnum(enum.Enum):
    video = "Video"
    image = "Image"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250),nullable=False)
    user_name = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    gender = Enum(GenderEnum)
    post=relationship("Post")
    user_Follower = relationship('User_Follower')

class User_Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    follower_id = (Integer, ForeignKey('user.id'))
    
    


class Post(Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(250),nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    created = relationship("User") 
    media = relationship("Media")
    
class Comment(Base): # relacion de muchos a muchos
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(150), nullable = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Enum(MediaEnum)
    url =  Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
