import unittest
from unittest.mock import MagicMock
from services.teacherSchedule import TeacherScheduleService
from tests.mock_teacher_schedule import BASE_SCHEDULE


class TestTeacherSchedule(unittest.TestCase):
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
