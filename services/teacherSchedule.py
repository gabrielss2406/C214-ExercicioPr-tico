import json

from models.Teacher import Teacher


def fetch_teacher_schedule() -> str:
    response = """
    {
        "nomeDoProfessor": "Jane Doe",
        "horarioDeAtendimento": "10:00 - 12:00",
        "periodo": "afternoon",
        "sala": "102",
        "predio": ["1"]
    }
    """
    return response


def create_teacher_from_json(json_string: str) -> Teacher:
    data = json.loads(json_string)

    return Teacher(
        name=data["nomeDoProfessor"],
        schedule=data["horarioDeAtendimento"],
        period=data["periodo"],
        room=data["sala"],
        building=data["predio"],
    )
