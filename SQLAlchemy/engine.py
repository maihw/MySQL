from sqlalchemy import create_engine
engine = create_engine('mysql://root@localhost/study? charset=utf8')

from sqlalchemy.ext.declarative import ceclarative_base
Base = declarative_base(engine)

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.name)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User',
            backref=backerf('course',casecade='all,delete-rophan'))
    def __repr__(self):
        return '<Course:{}>.format(self.name)

