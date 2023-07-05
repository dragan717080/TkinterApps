from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    @staticmethod
    def get_session():
        engine = create_engine('sqlite:///sqlalchemy_tables.db')
        Session = sessionmaker(bind=engine)
        return Session()

    @classmethod
    def find(cls, **kwargs):
        session = cls.get_session()
        continent = session.query(cls).filter_by(**kwargs).first()
        session.close()
        return continent

    @classmethod
    def find_all(cls):
        session = cls.get_session()
        continents = session.query(cls).all()
        session.close()
        return continents

    @classmethod
    def save(cls, self):
        session = cls.get_session()
        session.add(self)
        session.commit()
        session.close()

    @classmethod
    def delete_all(cls):
        session = cls.get_session()
        session.query(cls).delete()
        session.commit()
        session.close()

class User(BaseModel):
    __bind_key__ = __tablename__ = 'users'
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)

class Continent(BaseModel):
    __bind_key__ = __tablename__ = 'continents'
    name = Column(String(50))
    fragile_states_index = Column(Float)
    factionalized_elites_index = Column(Float)
    military_spending_percentage_index = Column(Float)
    oil_reserves_index = Column(Float)

engine = create_engine('sqlite:///sqlalchemy_tables.db')
Base.metadata.bind = engine

Base.metadata.create_all(bind=engine)
