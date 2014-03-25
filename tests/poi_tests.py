import os
import sys
sys.path.append(os.path.abspath('..'))

from poiguardians.poi import *

import unittest

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'


class test_poi(unittest.TestCase):
    """Tests for the Poi object"""

    def test_load_poi(self):
        poi_list = Poi.load_poi_file('testdata-poi.txt')
        # for poi in poi_list:
            # print(poi.ptype, poi.level, poi.coords)
        self.assertIsNotNone(poi_list, 'POI list not loading')
        # print(poi_list[0].ptype)
        self.assertEqual(poi_list[0].ptype, 'Tiberium', 'POI type not set')
        # print(poi_list[2].ptype)
        self.assertEqual(poi_list[5].ptype, 'Crystal', 'POI type not set')
        self.assertEqual(len(poi_list), 22, 'Not all POI loaded')

    def test_poi_distance(self):
        poi_list = Poi.load_poi_file('testdata-poi.txt')
        # print(round(poi_list[0].distance(poi_list[1].coords),2))
        self.assertEqual(round(poi_list[0].distance(poi_list[1].coords),2), 37.8, 'Distance incorrect')

if __name__ == '__main__':
    unittest.main()
