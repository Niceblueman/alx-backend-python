import unittest
from unittest.mock import patch
import io
import asyncio
from importlib import import_module

async_generator_module = import_module('0_async_generator')
async_generator = async_generator_module.async_generator
print_yielded_values = async_generator_module.print_yielded_values

class TestAsyncGenerator(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_yielded_values(self, mock_stdout):
        expected_output = "[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]\n"
        asyncio.run(print_yielded_values())
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
