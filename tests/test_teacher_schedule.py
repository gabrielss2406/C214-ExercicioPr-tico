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
            "sala": "1",
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
        self.assertEqual(teacher.room, "1", "A sala do professor está incorreta")
        self.assertEqual(
            teacher.building, ["1"], "O prédio do professor está incorreto"
        )

    def test_teachers_building_array_size(self):
        teacher = create_teacher_from_json(self.mock_json)

        self.assertEqual(
            len(teacher.building), 1,
            "Um professor pode trabalhar em apenas um prédio"
        )

    def test_teachers_building_range(self):
        teacher = create_teacher_from_json(self.mock_json)

        self.assertTrue(
            1 <= int(teacher.building[0]) <= 6,
            f"O prédio {teacher.building[0]} está fora da faixa 1 até 6 de prédios disponíveis"
        )

    def test_teachers_room_range(self):
        teacher = create_teacher_from_json(self.mock_json)

        self.assertTrue(
            1 <= int(teacher.room) <= 30,
            f"A sala {int(teacher.room)} está fora da faixa de 1 até 30 de salas disponíveis"
        )

    def test_teachers_room_and_building_logic(self):
        teacher = create_teacher_from_json(self.mock_json)

        buildings = ["1", "2", "3", "4", "5", "6"]

        for i in range(len(buildings)):
            if teacher.building[0] == buildings[i]:
                self.assertTrue(
                    5 * i + 1 <= int(teacher.room) <= 5 * (i + 1),
                    "A sala do professor não bate com o prédio estabelecido"
                )

        # if 1 <= int(teacher.room) <= 5:
        #     self.assertEqual(teacher.building[0], "1")
        # elif 6 <= int(teacher.room) <= 10:
        #     self.assertEqual(teacher.building[0], "2")
        # elif 11 <= int(teacher.room) <= 15:
        #     self.assertEqual(teacher.building[0], "3")
        # elif 16 <= int(teacher.room) <= 20:
        #     self.assertEqual(teacher.building[0], "4")
        # elif 21 <= int(teacher.room) <= 25:
        #     self.assertEqual(teacher.building[0], "5")
        # elif 26 <= int(teacher.room) <= 30:
        #     self.assertEqual(teacher.building[0], "6")
