import graphene
import graphene as g
from graphene import DateTime

from db.database import db_session
from db.models import CityModel
from db.models.mission import MissionModel
from db.models.target import TargetModel
from db.models.country import CountryModel
from db.models.targettypes import TargetTypesModel
from graphene_sqlalchemy import SQLAlchemyObjectType

from db.models.target import TargetModel


class Missions(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node, )

class Targets(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (graphene.relay.Node, )

class Countries(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node, )

class Query(g.ObjectType):
    mission_by_id = g.Field(Missions, _id=g.Int(required=True))
    missions_by_dates_range = g.List(Missions,start_date=g.Date(required=True), end_date=g.Date(required=True))
    missions_by_countries = g.List(Missions, country_id=g.Int(required=True))
    missions_by_targets_industry = g.List(Missions, targetIndustry=g.String(required=True))
    attack_results_by_type = g.List(Missions, target_type_name=g.String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, _id):
         return db_session.query(MissionModel).get(_id)

    @staticmethod
    def resolve_missions_by_dates_range(root, info,  start_date, end_date):
         return db_session.query(MissionModel).filter(MissionModel.mission_date.between(start_date, end_date)).all()
    #
    @staticmethod
    def resolve_missions_by_countries(root, info, country_id):
        return (db_session.query(MissionModel)
                .join(MissionModel.targets)
                .join(TargetModel.cities)
                .join(CityModel.countries)
                .filter(CountryModel.country_id == country_id)
                .all())


    @staticmethod
    def resolve_missions_by_targets_industry(root, info, targetIndustry):
        return (db_session.query(MissionModel)
                .join(MissionModel.targets)
                .filter(
                        TargetModel.target_industry == targetIndustry
                ).all()
                )

    @staticmethod
    def resolve_attack_results_by_type(root, info, target_type_name):
        return (db_session.query(MissionModel).
                join(MissionModel.targets)
                .join(TargetModel.targettypes)
                .filter(TargetTypesModel.target_type_name == target_type_name)
                .all())