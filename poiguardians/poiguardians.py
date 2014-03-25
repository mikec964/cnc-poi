import os
import csv

import poi
import base

"""This program ensures that each POI has a defender.

It will identify the nearest defender and the range, so you can issue orders
to move them closer.

Print a list of orders to move players to assigned bases.
Draw a map.
Report how many players are within 20 of a POI.
List POIs within 20 of a player.
List outlying POIs.
"""

def main():
    poi_list = poi.Poi.load_poi_file('poi.txt', '../data')
    for poi1 in poi_list:
        closest_distance = 9999
        closest_poi = None
        for poi2 in poi_list:
            if poi1.coords != poi2.coords:
                dist = poi1.distance(poi2.coords)
                if dist < closest_distance:
                    closest_distance = dist
                    closest_poi = poi2
        print(int(closest_distance), poi1.ptype, poi1.coords, closest_poi.ptype, closest_poi.coords)

    base_list = base.Base.load_file('bases.csv', '../data')
    for pbase in base_list:
        pbase.print_table()

if __name__ == "__main__":
    main()
