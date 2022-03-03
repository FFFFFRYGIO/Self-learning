from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, null
from sqlalchemy.orm import relationship
from create_and_connect import Base, db, session

class List(Base):
    __tablename__ = 'list'
    lid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    priority = Column(Integer, nullable=True)

class ListUser(Base):
    __tablename__ = 'listuser'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    UniqueConstraint(email)

class Users_of_list(Base):
    __tablename__ = 'users_of_list'
    user_id = Column(Integer, ForeignKey('listuser.uid'), primary_key=True, nullable=False)
    list_id = Column(Integer, ForeignKey('list.lid'), primary_key=True, nullable=False)
    user_id_r = relationship('ListUser', backref='user_of_list')
    list_id_r = relationship('List', backref='list_user_manage')
    UniqueConstraint(user_id, list_id)

class Task(Base):
    __tablename__ = 'task'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    list_id = Column(Integer, ForeignKey('list.lid'), nullable=False)
    description = Column(String(50), nullable=False)
    is_done = Column(Boolean, nullable=False, default=False)
    list_id_r = relationship('List', backref='list_with_task')

Base.metadata.create_all(db)