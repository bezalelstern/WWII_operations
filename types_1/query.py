import graphene

from types.mission_type import MissionType


class Query(graphene.ObjectType):
    mission_by_id = graphene.Field(MissionType, id=graphene.Int(required=True))