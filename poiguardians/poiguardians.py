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
    poi_list = poi.Poi.load_file('poi.txt', '../data')
    print("#### POI LIST ####")
    for poi1 in poi_list:
        poi1.print_table()

    base_list = base.Base.load_file('bases.csv', '../data')
    print("\n#### BASE LIST ####")
    for base1 in base_list:
        base1.print_table()

    print("\n### POI TO BASE LIST ####")
    for poi1 in poi_list:
        closest_distance = 9999
        closest_base = None
        for base1 in base_list:
            dist = poi1.distance(base1.coords)
            if dist < closest_distance:
                closest_distance = dist
                closest_base = base
        # print(int(closest_distance), poi1.ptype, poi1.coords, closest_base.name, closest_base.coords)

if __name__ == "__main__":
    main()
