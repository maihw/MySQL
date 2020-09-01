from sqlalchemy.orm import sessionmaker
from base import Base, engine, User, Course

session = sessionmaker(engine)()
