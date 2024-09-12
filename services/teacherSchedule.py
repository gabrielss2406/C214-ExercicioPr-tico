from typing import Union
import requests
import json
from models.Teacher import Teacher


class TeacherScheduleService:
    def __init__(self, data):
        if isinstance(data, str):
            data = json.loads(data)

        self.name = data["nomeDoProfessor"]
        self.schedule = data["horarioDeAtendimento"]
        self.period = data["periodo"]
        self.room = data["sala"]
        self.building = data["predio"]

    def fetch_teacher_schedule(self) -> Union[str, None]:
        response = requests.get("https://api.example.com/teacher/schedule")

        if response.status_code == 200:
            return response.text
        else:
            return None

    def create_teacher_from_json(json_string: str) -> Teacher:
        data = json.loads(json_string)

        return Teacher(
            name=data["nomeDoProfessor"],
            schedule=data["horarioDeAtendimento"],
            period=data["periodo"],
            room=data["sala"],
            building=data["predio"],
        )

    def assign_building(self, room: str, build: str):
        return 5 * build + 1 <= int(room) <= 5 * (build + 1)
