"""End-to-end smoke test across the three live services.

Flow: create a question -> vote on it -> view it show up in polls.
Also checks the one real cross-service rule: voting on a question id
that doesn't exist must be rejected.

Requires the stack to already be running (`make up` / `docker compose up`,
or three `manage.py runserver`s) on the default ports, and the `requests`
package (already a dependency of each service). Override QUESTION_URL /
VOTE_URL / POLL_URL to point elsewhere.

    python tests/test_integration.py
"""

import os
import unittest
import requests

QUESTION_URL = os.environ.get("QUESTION_URL", "http://localhost:8002")
VOTE_URL = os.environ.get("VOTE_URL", "http://localhost:8003")
POLL_URL = os.environ.get("POLL_URL", "http://localhost:8001")


class ServiceIntegrationTests(unittest.TestCase):
    def test_create_question_then_vote_then_view_poll(self):
        response = requests.post(
            f"{QUESTION_URL}/question/", json={"questions": "Best language?"}
        )
        self.assertEqual(response.status_code, 201, response.text)
        question_id = response.json()["id"]

        response = requests.post(f"{VOTE_URL}/vote/", json={"question_id": question_id})
        self.assertEqual(response.status_code, 201, response.text)
        self.assertEqual(response.json()["question_id"], question_id)

        response = requests.post(
            f"{POLL_URL}/poll/", json={"vote": 1.0, "category": "languages"}
        )
        self.assertEqual(response.status_code, 201, response.text)

        response = requests.get(f"{POLL_URL}/poll/")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(any(p["category"] == "languages" for p in response.json()))

    def test_vote_rejects_unknown_question(self):
        response = requests.post(
            f"{VOTE_URL}/vote/", json={"question_id": "000000000000000000000000"}
        )
        self.assertEqual(response.status_code, 400, response.text)


if __name__ == "__main__":
    unittest.main()
