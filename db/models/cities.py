from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.models import Base


class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    latitude = Column(Float)
    longitude = Column(Float)
    targets = relationship("TargetModel", back_populates="cities")

    countries = relationship("CountryModel",back_populates="cities")