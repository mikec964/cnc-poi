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

def bases_with_attack(base_list, attack):
    possible_guardians = []
    for b in base_list:
        if b.attack > 10:
            possible_guardians.append(b)
    # print(possible_guardians[0].name)
    # print(possible_guardians[1].name)
    return possible_guardians

def bases_without_player(base_list, player):
    selected_bases = []
    for b in base_list:
        if b.owner != player:
            selected_bases.append(b)
    return selected_bases

def main():
    poi_list = poi.Poi.load_file('poi.txt', '../data')
    print("#### POI LIST ({0}) ####".format(len(poi_list)))
    for poi1 in poi_list:
        poi1.print_table()

    base_list = base.Base.load_file('bases.csv', '../data')
    print("\n#### BASE LIST ({0}) ####".format(len(base_list)))
    for base1 in base_list:
        base1.print_table()

    # Remove weak offense (possible RP farms) from possible guardians
    possible_guardians = bases_with_attack(base_list, 10)

    # Automatically assign adjacent bases to be guardian
    # Only 1 guardian per player
    guardians = {}
    for poi1 in poi_list:
        # print(poi1.ptype, poi1.level),
        closest_distance = 9999
        closest_base = None
        # find closest base
        for base1 in possible_guardians:
            # print(base1.name),
            dist = poi1.distance(base1.coords)
            if dist < closest_distance:
                closest_distance = dist
                closest_base = base1
        # assign to poi
        guardians[poi1.coords] = closest_base
        # print()
        # print(closest_base.name, 'assigned to', poi1.ptype, poi1.level)
        # If possible, remove player from possible_guardians
        possible_guardians = bases_without_player(possible_guardians, closest_base.owner)
        if possible_guardians == []:
            possible_guardians = bases_with_attack(base_list, 10)

    # Print Poi list
    print("\n### POI AND ASSIGNED GUARDIANS ####")
    for poi1 in poi_list:
        print("{0}({1}) at {2} guarded by {3}/{4} at {5}, range {6}".format(
            poi1.ptype, poi1.level, poi1.coords,
            guardians[poi1.coords].owner, guardians[poi1.coords].name,
            guardians[poi1.coords].coords,
            poi1.distance(guardians[poi1.coords].coords)))
    # Print marching orders, sort by player


if __name__ == "__main__":
    main()
