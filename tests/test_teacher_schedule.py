import unittest
from unittest.mock import patch
from services.teacherSchedule import fetch_teacher_schedule, create_teacher_from_json

        # JSON MOCK

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

        # TESTES API

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
        
        # TESTES "CERTOS"
        
    def test_create_teacher_from_json_name_correct(self):
        # Testando se o nome do professor é criado corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)
        self.assertEqual(teacher.name, "John Doe", "O nome do professor está correto")

    def test_create_teacher_from_json_schedule_correct(self):
        # Testando se o horário de atendimento do professor é criado corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)
        self.assertEqual(teacher.schedule, "09:00 - 12:00", "O horário do professor está correto")

    def test_create_teacher_from_json_period_correct(self):
        # Testando se o período do professor é criado corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)
        self.assertEqual(teacher.period, "morning", "O período do professor está correto")

    def test_create_teacher_from_json_room_correct(self):
        # Testando se a sala do professor é criada corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)
        self.assertEqual(teacher.room, "101", "A sala do professor está correta")

    def test_create_teacher_from_json_building_correct(self):
        # Testando se o prédio do professor é criado corretamente a partir do JSON
        teacher = create_teacher_from_json(self.mock_json)
        self.assertEqual(teacher.building, ["1"], "O prédio do professor está correto")
        
        # TESTES "ERRADOS"

    def test_create_teacher_from_json_name_incorrect(self):
        # Testando se o nome do professor é criado incorretamente
        teacher = create_teacher_from_json(self.mock_json)
        self.assertNotEqual(teacher.name, "Jane Doe", "O nome do professor está incorreto")

    def test_create_teacher_from_json_schedule_incorrect(self):
        # Testando se o horário de atendimento do professor é criado incorretamente
        teacher = create_teacher_from_json(self.mock_json)
        self.assertNotEqual(teacher.schedule, "10:00 - 13:00", "O horário do professor está incorreto")

    def test_create_teacher_from_json_period_incorrect(self):
        # Testando se o período do professor é criado incorretamente
        teacher = create_teacher_from_json(self.mock_json)
        self.assertNotEqual(teacher.period, "afternoon", "O período do professor está incorreto")

    def test_create_teacher_from_json_room_incorrect(self):
        # Testando se a sala do professor é criada incorretamente
        teacher = create_teacher_from_json(self.mock_json)
        self.assertNotEqual(teacher.room, "102", "A sala do professor está incorreta")

    def test_create_teacher_from_json_building_incorrect(self):
        # Testando se o prédio do professor é criado incorretamente
        teacher = create_teacher_from_json(self.mock_json)
        self.assertNotEqual(teacher.building, ["2"], "O prédio do professor está incorreto")
