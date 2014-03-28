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

def bases_not_rp_farms(base_list):
    """Return a list of bases that aren't RP farms"""

    possible_guardians = []
    for b in base_list:
        if not ((b.name.upper().find("RP") != -1) \
        and (b.name.upper().find("RPKING") == -1)):
            # print b.name
            possible_guardians.append(b)
    return possible_guardians

def bases_with_defense(base_list, defense):
    """Return a list of bases with at least a certain defense value"""

    possible_guardians = []
    for b in base_list:
        # print(b.name, "-", b.defense, ">=", defense, int(b.defense) >= int(defense))
        if (b.defense >= defense):
            possible_guardians.append(b)
    # print(possible_guardians[0].name)
    # print(possible_guardians[1].name)
    return possible_guardians

def bases_with_attack(base_list, attack):
    """Return a list of bases with at least a certain attack value"""

    possible_guardians = []
    for b in base_list:
        if b.attack > attack:
            possible_guardians.append(b)
    # print(possible_guardians[0].name)
    # print(possible_guardians[1].name)
    return possible_guardians

def bases_without_player(base_list, player):
    """Return a list of bases that are NOT owned by a particular player"""

    selected_bases = []
    for b in base_list:
        if b.owner != player:
            selected_bases.append(b)
    return selected_bases

def assign_bases(poi_list, base_list):
    """Assign bases to guard POI

    Follow a set of rules:
    a) Automatically assign bases adjacent to a POI to guard that POI
    b) Try to only use 1 base from a player to be a guardian
    x) Don't assign RP farms or weak defense bases to be guardians
    x) Pick the strongest players first, so they don't move so far
    e) Try to assign the closest qualified base
    """

    guardians = {}
    possible_guardians = base_list
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
    return guardians


def main():
    poi_list = poi.Poi.load_file('poi.txt', '../data')
    print("#### POI LIST ({0}) ####".format(len(poi_list)))
    for poi1 in poi_list:
        poi1.print_email()

    base_list = base.Base.load_file('ASY2 base list - Form Responses 1.csv', '../data')
    print("\n#### BASE LIST ({0}) ####".format(len(base_list)))
    for base1 in base_list:
        base1.print_table()

    poi_dict = {}
    for p in poi_list:
        poi_dict[p.coords] = p

    possible_guardians = bases_not_rp_farms(base_list)
    possible_guardians = bases_with_defense(possible_guardians, 15)
    guardians = assign_bases(poi_list, possible_guardians)

    # Print Poi list
    print("\n#### POI AND ASSIGNED GUARDIANS ####")
    for poi1 in poi_list:
        print("{0}-{1} at {2} guarded by {3}/{4} at {5}, range {6}".format(
            poi1.ptype, poi1.level, poi1.coords_link(),
            guardians[poi1.coords].owner, guardians[poi1.coords].name,
            guardians[poi1.coords].coords_link(),
            poi1.distance(guardians[poi1.coords].coords)))

    # Print marching orders, sort by player
    print("\n#### MARCHING ORDERS ####")
    for coords in guardians.keys():
        base1 = guardians[coords]
        print("{0}, move {1} at {2} to the {3}-{4} at {5}".format(
            base1.owner_link(), base1.name, base1.coords_link(),
            poi_dict[coords].ptype, poi_dict[coords].level,
            poi_dict[coords].coords_link()
            ))

if __name__ == "__main__":
    main()
