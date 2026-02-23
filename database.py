from sqlalchemy import create_engine, declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection settings
database_url = 'postgresql://username:password@localhost/dbname'

# Create a new database engine instance
engine = create_engine(database_url)

# Create a declarative base class
Base = declarative_base()

# Setup session maker
Session = sessionmaker(bind=engine)