import unittest

from parser import Parser
from collections import OrderedDict


class TestSum(unittest.TestCase):

    def test_cron_parser_scenario_one(self):
        parser = Parser("*/15 0 1,15 * 1-5 /usr/bin/find")
        expected_output = {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day_month": [1, 15],
            "month": list(range(1, 13)),
            "day_week": [1, 2, 3, 4, 5],
            "command": "/usr/bin/find"
        }
        self.assertEqual(parser.split_and_parse(), expected_output)

    def test_cron_parser_scenario_two(self):
        parser = Parser("23 0-20/2 * * * /usr/bin/find")
        expected_output = OrderedDict({
            "minute": [23],
            "hour": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
            "day_month": list(range(1, 31)),
            "month": list(range(1, 13)),
            "day_week": [1, 2, 3, 4, 5, 6, 7],
            "command": "/usr/bin/find"
        })
        self.assertEqual(parser.split_and_parse(), expected_output)


if __name__ == '__main__':
    unittest.main()
