from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.models import Base


class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    target_priority = Column(Integer)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey("targettypes.target_type_id"))
    cities = relationship("CityModel", back_populates="targets")
    missions = relationship("MissionModel", back_populates="targets")
    targettypes = relationship("TargetTypesModel", back_populates="targets")
