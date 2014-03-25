import os
import sys
sys.path.append(os.path.abspath('..'))

from poiguardians.base import *

import unittest

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'


class test_base(unittest.TestCase):
    """ Tests for the Base object"""

    def test_load_base(self):
        base_list = Base.load_file('testdata-bases.csv')
        self.assertIsNotNone(base_list, 'Base list not loading')
        self.assertEqual(base_list[0].owner, 'xbrDeckard', 'Incorrect field parsing')
        for base in base_list:
            # base.print_csv()
            # base.print_table()
            self.assertNotEqual(base.name,'', 'Not ignoring blank bases')
        x, y = base_list[0].coords
        self.assertEqual(x,657)
        self.assertEqual(y,227)


if __name__ == '__main__':
    unittest.main()
