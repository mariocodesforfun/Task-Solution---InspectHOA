#creating the database tables
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


# from sqlalchemy.orm import sessionmaker


class Roles(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key=True, nullable=False)
    role_name = Column(String(255), nullable=False)
    role_description = Column(String(255), nullable=False)

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    account_password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.role_id"))

class Properties(Base):
    __tablename__ = "properties"

    prop_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    prop_address = Column(String(255), nullable=False)
    prop_city = Column(String(255), nullable=False) 
    prop_state = Column(String(255), nullable=False) 
    prop_email = Column(String(255), nullable=False) 


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, nullable=False)
    prop_id = Column(Integer, ForeignKey('properties.prop_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    doc_name = Column(String(255), nullable=False)
    order_status = Column(String(255), nullable=False)




#creating the objects(tables):
# Base.metadata.create_all(engine)