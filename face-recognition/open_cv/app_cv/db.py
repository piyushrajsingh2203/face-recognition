from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://postgres:piyush%402203#@localhost:5432/postgres"  # (%40) this is use for @ in my password.  # Replace with your PostgreSQL credentials

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Create the images directory if it does not exist
os.makedirs("images", exist_ok=True)