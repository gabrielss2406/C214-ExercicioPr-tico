import unittest
from unittest.mock import MagicMock, patch

from services.teacherSchedule import TeacherScheduleService
from tests.mock_teacher_schedule import BASE_SCHEDULE


class TestTeacherSchedule(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock()
        self.mock_service.return_value = BASE_SCHEDULE
        self.service = TeacherScheduleService(data=self.mock_service.return_value)

    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_success(self, mock_get):
        # Simulando o retorno da API com sucesso (status 200)
        mock_get.return_value.status_code = 200

        self.assertIsNotNone(
            self.service, "A função não deve retornar None para status 200"
        )

    @patch("services.teacherSchedule.requests.get")
    def test_fetch_teacher_schedule_failure(self, mock_get):
        # Simulando uma falha na API (status 404)
        mock_get.return_value.status_code = 404

        result = self.service.fetch_teacher_schedule()

        self.assertIsNone(result, "A função deve retornar None para status 404")
