from graphene import ObjectType, Int, String, Field, Float


class MissionType(ObjectType):
    mission_id = Int(required=True)
    mission_date = String()
    airborne_aircraft = String()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()