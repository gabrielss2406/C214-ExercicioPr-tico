import requests
import json
from models.Teacher import Teacher


def fetch_teacher_schedule() -> [str, None]:
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
