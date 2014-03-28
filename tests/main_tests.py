import os
import sys
sys.path.append(os.path.abspath('..'))

from poiguardians.poiguardians import *
from poiguardians.base import *
from poiguardians.poi import *

import StringIO
import unittest

class test_poiguardians(unittest.TestCase):
    """Tests for the main poiguardians code"""

    def test_bases_not_rp_farms(self):
        base_list = Base.load_file('testdata-bases.csv')
        guardians = bases_not_rp_farms(base_list)
        for base in guardians:
            self.assertNotEqual(base.name, 'RPFarm 1.3M')
        rpking = False
        for base in guardians:
            if base.name.find('RPKing'):
                rpking = True
        self.assertTrue(rpking)

    def test_bases_with_defense(self):
        base_list = Base.load_file('testdata-bases.csv')
        defense = 22
        guardians = bases_with_defense(base_list, defense)
        for base in guardians:
            # print base.name, base.defense
            pass
        self.assertEqual(guardians[0].name, 'RPFarm 1.3M')

    def test_bases_with_attack(self):
        base_list = Base.load_file('testdata-bases.csv')
        attack = 10
        guardians = bases_with_attack(base_list, attack)
        self.assertEqual(guardians[0].name, 'Blade Runner')

if __name__ == '__main__':
    unittest.main()
