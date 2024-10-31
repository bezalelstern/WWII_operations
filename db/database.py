from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session

from db.models import Base

URL = "postgresql://admin:1234@localhost:5437/missions_db"

engine = create_engine(URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DB_URL
# #from db.data import employee_data, jobs_data
# from db.models import Base
#
# engine = create_engine(DB_URL)
# Session_maker = sessionmaker(bind=engine)
#
#
# def init_db():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#     with Session_maker() as session:
#         session.commit()
