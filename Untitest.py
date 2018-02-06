from unittest.mock import patch
import unittest

from . import BattleShip

class ContainersTestCase(unittest.TestCase):

    def test_get_input_stacks_processed_input_correctly(self):
        user_input = [
            '3',
            '4 1 2 3 2',
            '1 2',
            '0',
        ]
        expected_stacks = [
            "Invalid size format."
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = battle_ship()
        self.assertEqual(stacks, expected_stacks)


if __name__ == '__main__':
    unittest.main()
