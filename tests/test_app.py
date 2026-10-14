"""Unit tests for the Flask service."""
import unittest

from service import app


class ServiceRoutesTest(unittest.TestCase):
    """Test public HTTP routes."""

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_index_reports_service_running(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "SERVICERUNNING")
        self.assertEqual(response.get_json()["port"], 8000)

    def test_health_is_ok(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "OK")


if __name__ == "__main__":
    unittest.main()
