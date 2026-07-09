from pydantic import BaseModel , ValidationError, Field
from datetime import datetime

class SpaceStation(BaseModel):
    station_id :str = Field(min_length=3, max_length=10)
    name :str = Field(min_length=1, max_length=50)
    crew_size :int = Field(ge=1, le=20)
    power_level :float = Field(ge=0, le=100)
    oxygen_level :float = Field(ge=0, le=100)
    last_maintenance : datetime
    is_operational: bool = Field(default=True)
    notes: str | None  = Field(min_length=0, max_length=200)

if __name__ == "__main__":
    station = {
        'station_id': 'LGW125',
        'name': 'Titan Mining Outpost',
        'crew_size': 20,
        'power_level': 76.4,
        'oxygen_level': 95.5,
        'last_maintenance': '2023-07-11T00:00:00',
        'is_operational': True,
        'notes': "None"
    }
    try:
        space_station: SpaceStation = SpaceStation.model_validate(station)
        print(space_station)
    except ValidationError as err:
        for e in err.errors():
            print(e.get('msg'))