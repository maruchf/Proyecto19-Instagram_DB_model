import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email= Column(String,unique=True,nullable=False)
    username = Column(String, unique=True, nullable=False)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    password= Column(String(15), nullable=False)
    #relación que permite al objeto hijo referirse al objeto padre directamente,usa el ForeingKey preestablecida
    posts= relationship("Post",backref="author")
    comments = relationship("Comment",backref="author_comment")
    posts_likes =relationship("PostLike",backref="author_post_like")
    comments_likes= relationship("CommentLike",backref="author_comment_like")


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String, unique=True, nullable=False)
    date_published = Column(DateTime, nullable=False)
    content = Column(String(300),nullable=True)
    latitude= Column(Float,nullable=True)
    longitude= Column(Float, nullable=True)
    likes=relationship("PostLike", backref="post")
    comments=relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(String(300),nullable=True)
    date_published = Column(DateTime, nullable=False)
    comment_likes = relationship("CommentLike", backref="comment")

class CommentLike(Base):
    __tablename__ = 'commentlike'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class PostLike(Base):
    __tablename__ = 'postlike'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')