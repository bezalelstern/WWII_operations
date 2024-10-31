from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .mission import MissionModel
from .target import TargetModel
from .cities import CityModel
from .country import CountryModel
from .targettypes import TargetTypesModel