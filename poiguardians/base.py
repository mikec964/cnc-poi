import os
import csv
import math

def load_csv(filename, directory=''):
    """Filter out commented lines"""

    csvlist = []
    filepath = os.path.join(directory, filename)
    # print(filepath)
    with open(filepath, 'U') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if (row[0][0] != '#'):
                    csvlist.append(row)
    return csvlist


class Base(object):
    """Bases have owners, attack, defense, and coordinates"""

    def __init__(self, owner, name, attack, defense, coords):
        self.owner = owner
        self.name = name
        self.attack = attack
        self.defense = defense
        self.coords = coords

    @classmethod
    def load_file(self, filename, directory=''):
        csv_list = load_csv(filename, directory)
        # Now, parse csv list of players into list of bases
        base_list = []
        for player in csv_list:
            if player[0] != 'Timestamp':
                coords = (int(player[5][0:3]), int(player[5][4:7]))
                base = Base(player[1], player[2], player[3], player[4], coords)
                base_list.append(base)

                if (player[6] != ''):
                    coords = (int(player[9][0:3]), int(player[9][4:7]))
                    base = Base(player[1], player[6], player[7], player[8], coords)
                    base_list.append(base)
                if (player[10] != ''):
                    coords = (int(player[13][0:3]), int(player[13][4:7]))
                    base = Base(player[1], player[10], player[11], player[12], coords)
                    base_list.append(base)
                if (player[14] != ''):
                    coords = (int(player[17][0:3]), int(player[17][4:7]))
                    base = Base(player[1], player[14], player[15], player[16], coords)
                    base_list.append(base)
        return base_list

    def print_csv(self):
        print("{0},{1},{2},{3},{4}".format(
            self.owner, self.name, self.attack, self.defense, self.coords))

    def print_table(self):
        print("{0:15} {1:20} {2:3} {3:3} {4}".format(
            self.owner, self.name, self.attack, self.defense, self.coords))

