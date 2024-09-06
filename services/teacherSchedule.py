import json

from models.Teacher import Teacher


def atribuir_predio(sala: int) -> str:
    if 1 <= sala <= 5:
        return "1"
    elif 6 <= sala <= 10:
        return "2"
    elif 11 <= sala <= 15:
        return "3"
    elif 16 <= sala <= 20:
        return "4"
    return "Desconhecido"


def popular_pagina(json_data: str) -> Teacher:
    """Recebe uma string JSON, processa, atribui o prédio e retorna um objeto Professor."""
    data = json.loads(json_data)
    predio = atribuir_predio(int(data["sala"]))
    professor = Teacher(
        nome=data["nomeDoProfessor"],
        horario=data["horarioDeAtendimento"],
        periodo=data["periodo"],
        sala=data["sala"],
        predio=predio,
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
