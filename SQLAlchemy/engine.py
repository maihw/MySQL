from sqlalchemy import create_engine
engine = create_engine('mysql://root@localhost/study? charset=utf8')

from sqlalchemy.ext.declarative import ceclarative_base
Base = declarative_base(engine)
