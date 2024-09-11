import unittest
from unittest.mock import patch
from services.teacherSchedule import fetch_teacher_schedule, create_teacher_from_json


class TestTeacherSchedule(unittest.TestCase):
    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_success(self, mock_get):
        # Simulando o retorno da API com sucesso (status 200)
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = """
        {
            "nomeDoProfessor": "John Doe",
            "horarioDeAtendimento": "09:00 - 12:00",
            "periodo": "morning",
            "sala": "101",
            "predio": ["1"]
        }
        """

        result = fetch_teacher_schedule()

        self.assertIsNotNone(result)
        self.assertIn("John Doe", result)

    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        result = fetch_teacher_schedule()

        self.assertIsNone(result)

    def test_create_teacher_from_json(self):
        mock_json = """
        {
            "nomeDoProfessor": "John Doe",
            "horarioDeAtendimento": "09:00 - 12:00",
            "periodo": "morning",
            "sala": "101",
            "predio": ["1"]
        }
        """
        teacher = create_teacher_from_json(mock_json)

        self.assertEqual(teacher.name, "John Doe")
        self.assertEqual(teacher.schedule, "09:00 - 12:00")
        self.assertEqual(teacher.period, "morning")
        self.assertEqual(teacher.room, "101")
        self.assertEqual(teacher.building, ["1"])


if __name__ == "__main__":
    unittest.main()
