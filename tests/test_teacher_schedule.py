import unittest
from unittest.mock import patch
from services.teacherSchedule import fetch_teacher_schedule, create_teacher_from_json


class TestTeacherSchedule(unittest.TestCase):
    def setUp(self):
        self.mock_json = """
        {
            "nomeDoProfessor": "John Doe",
            "horarioDeAtendimento": "09:00 - 12:00",
            "periodo": "morning",
            "sala": "101",
            "predio": ["1"]
        }
        """

    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_success(self, mock_get):
        # Simulando o retorno da API com sucesso (status 200)
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.mock_json

        result = fetch_teacher_schedule()

        self.assertIsNotNone(result, "A função não deve retornar None para status 200")
        self.assertIn(
            "John Doe", result, "O nome do professor esperado não está na resposta"
        )

    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_failure(self, mock_get):
        # Simulando uma falha na API (status 404)
        mock_get.return_value.status_code = 404

        result = fetch_teacher_schedule()

        self.assertIsNone(result, "A função deve retornar None para status 404")

    def test_create_teacher_from_json_creates_teacher_object_correctly(self):
        # Testando se o objeto Teacher é criado corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)

        self.assertEqual(teacher.name, "John Doe", "O nome do professor está incorreto")
        self.assertEqual(
            teacher.schedule, "09:00 - 12:00", "O horário do professor está incorreto"
        )
        self.assertEqual(
            teacher.period, "morning", "O período do professor está incorreto"
        )
        self.assertEqual(teacher.room, "101", "A sala do professor está incorreta")
        self.assertEqual(
            teacher.building, ["1"], "O prédio do professor está incorreto"
        )
