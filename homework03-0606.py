"""from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mssql+pymssql://dbadmin:Qwerty123@smx2024.database.windows.net:1433/dataAnalytics")
Session = sessionmaker(bind=engine)
sesija = Session()
Base = declarative_base()

class Students(Base):
    __tablename__ = "students_sanja"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    year = Column(Integer)
    grade_macedonian = Column(Integer)
    grade_math = Column(Integer)
    grade_english = Column(Integer)


class Teachers(Base):
    __tablename__ = "teachers_sanja"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    specialty = Column(String)


class Subjects(Base):
    __tablename__ = "subjects_sanja"

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    teacher_id = (Integer)


Base.metadata.create_all(engine)"""
    