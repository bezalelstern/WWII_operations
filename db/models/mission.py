from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from db.models import Base


class MissionModel(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(String, nullable=True)
    airborne_aircraft = Column(Float, nullable=True)
    attacking_aircraft = Column(Float, nullable=True)
    bombing_aircraft = Column(Float, nullable=True)
    aircraft_returned = Column(Float, nullable=True)
    aircraft_failed = Column(Float, nullable=True)
    aircraft_damaged = Column(Float, nullable=True)
    aircraft_lost = Column(Float, nullable=True)
    targets = relationship("TargetModel", back_populates="missions")
