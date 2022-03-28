from sqlalchemy import Column, Integer, String
from .Model import Model
from .mixins.TimestampMixin import TimestampMixin


class User(Model, TimestampMixin):
    __tablename__ = 'users'

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
