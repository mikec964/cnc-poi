import os
import sys
sys.path.append(os.path.abspath('..'))

from poiguardians.base import *

import unittest

# It's a mess, but appending to the sys path allows you to run this directly.
# Without it, you'd need this in the Python:
# from ..poiguardians.base import *
# And you'd do this from the command line:
    # To run these tests, cd to the PARENT of poiguardians, then:
    # python -m poiguardians.tests.base_tests


class test_base(unittest.TestCase):
    """ Tests for the Base object"""

    def test_load_base(self):
        base_list = Base.load_base_file('testdata-bases.csv')
        self.assertIsNotNone(base_list, 'Base list not loading')
        self.assertEqual(base_list[0].owner, 'xbrDeckard', 'Incorrect field parsing')
        for base in base_list:
            # base.print_csv()
            base.print_table()
            self.assertNotEqual(base.name,'', 'Not ignoring blank bases')

if __name__ == '__main__':
    unittest.main()
