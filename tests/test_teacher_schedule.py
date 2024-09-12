import unittest
from unittest.mock import MagicMock
from services.teacherSchedule import TeacherScheduleService
from tests.mock_teacher_schedule import BASE_SCHEDULE


class TestTeacherSchedule(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock()
        self.mock_service.return_value = BASE_SCHEDULE
        self.service = TeacherScheduleService(data=self.mock_service.return_value)

    def test_create_teacher_from_json_schedule_correct(self):
        # Testando se o horário de atendimento do professor é criado corretamente a partir do JSON
        self.assertEqual(
            self.service.schedule,
            "09:00 - 12:00",
            "O horário do professor está correto",
        )

        self.assertEqual(
            self.service.name, "John Doe", "O nome do professor está incorreto"
        )
        self.assertEqual(
            self.service.schedule,
            "09:00 - 12:00",
            "O horário do professor está incorreto",
        )
        self.assertEqual(
            self.service.period, "morning", "O período do professor está incorreto"
        )
        self.assertEqual(self.service.room, "1", "A sala do professor está incorreta")
        self.assertEqual(
            self.service.building, ["1"], "O prédio do professor está incorreto"
        )

    def test_create_teacher_from_json_name_correct(self):
        # Testando se o nome do professor é criado corretamente a partir do JSON
        self.assertEqual(
            self.service.name, "John Doe", "O nome do professor está correto"
        )

    def test_create_teacher_from_json_period_correct(self):
        # Testando se o período do professor é criado corretamente a partir do JSON
        self.assertEqual(
            self.service.period, "morning", "O período do professor está correto"
        )

    def test_create_teacher_from_json_room_correct(self):
        # Testando se a sala do professor é criada corretamente a partir do JSON
        self.assertEqual(self.service.room, "1", "A sala do professor está correta")

    def test_create_teacher_from_json_building_correct(self):
        # Testando se o prédio do professor é criado corretamente a partir do JSON
        self.assertEqual(
            self.service.building, ["1"], "O prédio do professor está correto"
        )

        # TESTES "ERRADOS"

    def test_create_teacher_from_json_name_incorrect(self):
        # Testando se o nome do professor é criado incorretamente
        self.assertNotEqual(
            self.service.name, "Jane Doe", "O nome do professor está incorreto"
        )

    def test_create_teacher_from_json_schedule_incorrect(self):
        # Testando se o horário de atendimento do professor é criado incorretamente
        self.assertNotEqual(
            self.service.schedule,
            "10:00 - 13:00",
            "O horário do professor está incorreto",
        )

    def test_create_teacher_from_json_period_incorrect(self):
        # Testando se o período do professor é criado incorretamente
        self.assertNotEqual(
            self.service.period, "afternoon", "O período do professor está incorreto"
        )

    def test_create_teacher_from_json_room_incorrect(self):
        # Testando se a sala do professor é criada incorretamente
        self.assertNotEqual(
            self.service.room, "102", "A sala do professor está incorreta"
        )

    def test_create_teacher_from_json_building_incorrect(self):
        # Testando se o prédio do professor é criado incorretamente
        self.assertNotEqual(
            self.service.building, ["2"], "O prédio do professor está incorreto"
        )
