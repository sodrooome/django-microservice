from unittest.mock import patch, Mock

import requests
from django.test import SimpleTestCase
from rest_framework.exceptions import ValidationError

from .serializers import VoteSerializer


class ValidateQuestionIdTests(SimpleTestCase):
    def setUp(self):
        self.serializer = VoteSerializer()

    @patch("vote.serializers.requests.get")
    def test_accepts_existing_question(self, mock_get):
        mock_get.return_value = Mock(status_code=200)
        self.assertEqual(self.serializer.validate_question_id("abc123"), "abc123")

    @patch("vote.serializers.requests.get")
    def test_rejects_missing_question(self, mock_get):
        mock_get.return_value = Mock(status_code=404)
        with self.assertRaises(ValidationError):
            self.serializer.validate_question_id("abc123")

    @patch("vote.serializers.requests.get")
    def test_rejects_when_service_unreachable(self, mock_get):
        mock_get.side_effect = requests.ConnectionError()
        with self.assertRaises(ValidationError):
            self.serializer.validate_question_id("abc123")
