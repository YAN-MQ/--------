import unittest
from src.chat.client import OllamaClient
from src.chat.models import ChatResponse

class TestOllamaClient(unittest.TestCase):
    def setUp(self):
        self.client = OllamaClient()

    def test_chat_response(self):
        response = self.client.chat("Hello")
        self.assertIsInstance(response, ChatResponse)
        self.assertIsNotNone(response.message)

if __name__ == '__main__':
    unittest.main()