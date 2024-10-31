import graphene

from db.database import db_session
from db.models import TargetModel
from db.models.mission  import MissionModel
from types_1.query import Missions


class AddTarget(graphene.Mutation):
    class Arguments:
        target_priority = graphene.Int()
        mission_id = graphene.Int(required=True)
        target_industry = graphene.String()
        city_id = graphene.Int(required=True)
        target_type_id = graphene.Int(required=True)

    target = graphene.Field(lambda: TargetModel)


    def mutate(self, info, target_priority, mission_id, target_industry, city_id, target_type_id):
        new_target = TargetModel(target_priority=target_priority,
                                  mission_id=mission_id,
                                  target_industry=target_industry,
                                  city_id=city_id,
                                  target_type_id=target_type_id)
        db_session.add(new_target)
        db_session.commit()
        return AddTarget(target=new_target)


class AddMission(graphene.Mutation):
    class Arguments:
        mission_date = graphene.String(required=True)
        airborne_aircraft = graphene.String(required=True)  # Format: 'YYYY-MM-DD'
        attacking_aircraft = graphene.Int(required=False)
        bombing_aircraft = graphene.Int(required=False)
        aircraft_returned = graphene.Int(required=False)
        aircraft_failed = graphene.Int(required=False)
        aircraft_damaged = graphene.Int(required=False)
        aircraft_lost = graphene.Int(required=False)

    user = graphene.Field(lambda: Missions)

    def mutate(self, info, mission_date, airborne_aircraft, attacking_aircraft,
               bombing_aircraft,aircraft_returned,aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        new_mission = MissionModel(mission_date=mission_date, airborne_aircraft=airborne_aircraft,
                                   attacking_aircraft=attacking_aircraft,bombing_aircraft=bombing_aircraft
                                   ,aircraft_returned=aircraft_returned,aircraft_failed =aircraft_failed
                                   ,aircraft_damaged=aircraft_damaged
                                   ,aircraft_lost=aircraft_lost)
        db_session.add(new_mission)
        db_session.commit()
        return AddMission(mission = new_mission)


class UpdateAttack(graphene.Mutation):
    class Arguments:
        mission_id = graphene.Int(required=True)
        returned_aircraft = graphene.Int()
        failed_aircraft = graphene.Int()
        damaged_aircraft = graphene.Int()
        lost_aircraft = graphene.Int()
        damage_assessment = graphene.Int()

    user = graphene.Field(lambda: Missions)

    def mutate(self, info, mission_id, returned_aircraft = None, failed_aircraft= None,
               damaged_aircraft =None, lost_aircraft = None, damage_assessment = None):
        mission = db_session.query(MissionModel).get(mission_id)
        if not mission:
            raise Exception("mission not found")
        mission.returned_aircraft = returned_aircraft
        mission.failed_aircraft = failed_aircraft
        mission.damaged_aircraft = damaged_aircraft
        mission.lost_aircraft = lost_aircraft
        mission.damage_assessment = damage_assessment
        db_session.commit()
        return UpdateAttack(mission=mission)


class DeleteMission(graphene.Mutation):
    class Arguments:

        mission_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, mission_id):
        mission = db_session.query(MissionModel).get(mission_id)
        if not mission:
            return DeleteMission(ok=False)
        db_session.delete(mission)
        db_session.commit()
        return DeleteMission(ok=True)


class Mutation(graphene.ObjectType):
    add_address = AddTarget.Field()
    add_mission = AddMission.Field()
    update_attack = UpdateAttack.Field()
    delete_mission = DeleteMission.Field()



