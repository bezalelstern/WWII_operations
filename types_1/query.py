import graphene
import graphene as g

from db.database import db_session
from db.models import Missions
from types_1.mission_type import MissionType
from graphene_sqlalchemy import SQLAlchemyObjectType

class User(SQLAlchemyObjectType):
    class Meta:
        model = Missions
        interfaces = (graphene.relay.Node, )

class Query(g.ObjectType):
    mission_by_id = g.Field(Missions, mission_id=g.Int(required=True))
    # missions_by_dates_range = g.List(Missions, start_date=g.String, end_date=g.String)
    # missions_by_countries = g.List(Missions, countries = g.String(required=True))
    # attack_results = g.List(Missions, target_type_name=g.String(required=True))

    # @staticmethod
    # def resolve_mission_by_id(mission_id):
    #     return db_session.query(Missions).filter(MissionType.mission_id == mission_id).first()
    #
    # @staticmethod
    # def resolve_missions_by_dates_range(start_date, end_date):
    #     pass
    #
    # @staticmethod
    # def resolve_missions_by_countries(countries):
    #     pass
    #     #return db_session.query(MissionType)