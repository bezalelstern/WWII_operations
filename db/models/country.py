from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from db.models import Base


class CountryModel(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    cities = relationship("CityModel", back_populates="countries")