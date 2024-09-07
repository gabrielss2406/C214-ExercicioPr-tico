from typing import List


class Teacher:
    def __init__(
        self, name: str, schedule: str, period: str, room: str, building: List
    ):
        if len(building) != 1:
            raise ValueError("Building array must have exactly one element")
        self.name = name
        self.schedule = schedule
        self.period = period
        self.room = room
        self.building = building
