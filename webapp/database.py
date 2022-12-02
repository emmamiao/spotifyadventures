from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///adventure.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    db_session.commit()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    song1 = Column(Integer, default = None)
    song2 = Column(Integer, default = None)
    song3 = Column(Integer, default = None)
    song4 = Column(Integer, default = None)
    song5 = Column(Integer, default = None)
    song6 = Column(Integer, default = None)
    song7 = Column(Integer, default = None)
    song8 = Column(Integer, default = None)
    song9 = Column(Integer, default = None)
    song10 = Column(Integer, default = None)

    def __init__(self, first_name=None, last_name=None, email=None, username=None, password=None, song1=None, song2=None, song3=None, song4=None, song5=None, song6=None, song7=None, song8=None,song9=None,song10=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.song1 = song1
        self.song2 = song2
        self.song3 = song3
        self.song4 = song4
        self.song5 = song5
        self.song6 = song6
        self.song7 = song7
        self.song8 = song8
        self.song9 = song9
        self.song10 = song10

    def __repr__(self):
        return f'<User {self.id!r}>'