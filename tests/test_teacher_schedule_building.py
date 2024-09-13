import unittest
from unittest.mock import MagicMock
from services.teacherSchedule import TeacherScheduleService
from tests.mock_teacher_schedule import BASE_SCHEDULE, BASE_WRONG_SCHEDULE


class TestTeacherScheduleBuilding(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock()
        self.mock_service.return_value = BASE_SCHEDULE
        self.service = TeacherScheduleService(data=self.mock_service.return_value)

    def test_teachers_building_array_size(self):
        self.assertEqual(
            len(self.service.building),
            1,
            "Um professor pode trabalhar em apenas um prédio",
        )

    def test_teachers_building_range(self):
        self.assertTrue(
            1 <= int(self.service.building[0]) <= 6,
            f"O prédio {self.service.building[0]} está fora da faixa 1 até 6 de prédios disponíveis",
        )

    def test_teachers_room_range(self):
        self.assertTrue(
            1 <= int(self.service.room) <= 30,
            f"A sala {int(self.service.room)} está fora da faixa de 1 até 30 de salas disponíveis",
        )

    def test_teachers_room_and_building_logic(self):
        buildings = ["1", "2", "3", "4", "5", "6"]

        for i in range(len(buildings)):
            if self.service.building[0] == buildings[i]:
                self.assertTrue(
                    self.service.assign_building(self.service.room, i),
                    "A sala do professor não bate com o prédio estabelecido",
                )


class TestTeacherScheduleBuildingWrong(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock()
        self.mock_service.return_value = BASE_WRONG_SCHEDULE
        self.service = TeacherScheduleService(data=self.mock_service.return_value)

    # Cenário negativo: Prédio fora da faixa esperada
    def test_teachers_building_out_of_range(self):
        self.assertFalse(
            1 <= int(self.service.building[0]) <= 6,
            f"O prédio {self.service.building[0]} está fora da faixa 1 até 6 de prédios disponíveis",
        )

    # Cenário negativo: Sala fora do intervalo válido
    def test_teachers_room_out_of_range(self):
        self.assertFalse(
            1 <= int(self.service.room) <= 30,
            f"A sala {int(self.service.room)} está fora da faixa de 1 até 30 de salas disponíveis",
        )

    # Cenário negativo: Lógica de associação entre sala e prédio falha
    def test_teachers_room_and_building_logic_failure(self):
        self.assertFalse(
            self.service.assign_building(self.service.room, self.service.building[0]),
            "A sala do professor não deveria bater com o prédio estabelecido",
        )

    # Cenário negativo: Array de building com mais de um elemento
    def test_teachers_building_with_more_than_one_element(self):
        self.service.building.append(100)
        self.assertNotEqual(
            len(self.service.building),
            1,
            "O array de prédios deve ter apenas um elemento",
        )
