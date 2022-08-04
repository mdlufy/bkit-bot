import unittest
from unittest.mock import patch
from datetime import datetime

class TestReset(unittest.TestCase):
    @patch('bot.cmd_reset', return_value="Начнем сначала. Как вас зовут?")
    def test_reset(self, cmd_reset):
        self.assertEqual(cmd_reset(self), "Начнем сначала. Как вас зовут?")

class TestData(unittest.TestCase):
    @patch('bot.send_data', return_value="20-12-2021")
    def test_data(self, send_data):
        self.assertEqual(send_data(self), datetime.now().strftime("%d-%m-%Y"))

if __name__ == "__main__":
    unittest.main()