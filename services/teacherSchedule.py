import json

from models.Teacher import Teacher


def assign_building(room: int) -> str:
    if 1 <= room <= 5:
        return "1"
    elif 6 <= room <= 10:
        return "2"
    elif 11 <= room <= 15:
        return "3"
    elif 16 <= room <= 20:
        return "4"
    return "Unkown"


def populate_page(json_data: str) -> Teacher:
    """Recebe uma string JSON, processa, atribui o prédio e retorna um objeto Professor."""
    data = json.loads(json_data)
    building = assign_building(int(data["sala"]))
    professor = Teacher(
        name=data["nomeDoProfessor"],
        schedule=data["horarioDeAtendimento"],
        period=data["periodo"],
        room=data["sala"],
        building=[building],
    )
    return professor


def create_teacher_from_json(json_string: str) -> Teacher:
    data = json.loads(json_string)

    return Teacher(
        name=data["nomeDoProfessor"],
        schedule=data["horarioDeAtendimento"],
        period=data["periodo"],
        room=data["sala"],
        building=data["predio"],
    )
