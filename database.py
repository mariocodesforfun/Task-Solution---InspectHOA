from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import settings


Base = declarative_base()




SQLACHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLACHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()







# session.add_all(user_data)
# session.add_all(properties_data)
# session.add_all(orders_data)

# Base.metadata.create_all(engine)


