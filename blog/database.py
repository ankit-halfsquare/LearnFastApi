from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



import pyodbc

server = '40.114.74.64,1401'
database = 'AM_PRIME_2_DEV'
username = 'amvmdev23'
password = 'AMvmdev-2023!'
driver= '{ODBC Driver 17 for SQL Server}' 



# connection_string = f"Driver={driver};Server=tcp:{server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
# SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={pyodbc.connect(connection_string)}"

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()