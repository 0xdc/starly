import pkgutil

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from .. import settings


engine = create_engine(str(settings.DATABASE_URL))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@as_declarative(bind=engine)
class Model(object):
    query = db_session.query_property()

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def save(self):
        db_session.add(self)
        db_session.commit()


for _, module_name, _ in pkgutil.walk_packages(__path__):
    __import__('.'.join([__name__, module_name]))
    del module_name
