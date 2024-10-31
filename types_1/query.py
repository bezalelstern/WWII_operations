import graphene
import graphene as g
from graphene import DateTime

from db.database import db_session
from db.models import Missions as MissionModel
from types_1.mission_type import MissionType
from graphene_sqlalchemy import SQLAlchemyObjectType

class Missions(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node, )

class Query(g.ObjectType):
    mission_by_id = g.Field(Missions, _id=g.Int(required=True))
    missions_by_dates_range = g.List(Missions,start_date=g.Date(required=True), end_date=g.Date(required=True))
    # missions_by_countries = g.List(Missions, countries = g.String(required=True))
    # attack_results = g.List(Missions, target_type_name=g.String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, _id):
         return db_session.query(MissionModel).get(_id)

    @staticmethod
    def resolve_missions_by_dates_range(root, info,  start_date, end_date):
         return db_session.query(MissionModel).filter(MissionModel.mission_date.between(start_date, end_date)).all()
    # #
    # @staticmethod
    # def resolve_missions_by_countries(countries):
    #     pass
    #     #return db_session.query(MissionType)