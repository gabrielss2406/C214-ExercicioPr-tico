from typing import List


class Teacher:
    def __init__(self, nome: str, horario: str, periodo: str, sala: str, predio: List):
        self.nome = nome
        self.horario = horario
        self.periodo = periodo
        self.sala = sala
        self.predio = predio
