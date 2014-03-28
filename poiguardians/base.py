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
                for i in [2, 6, 10, 14]:
                    if (player[i] != ''):
                        x = Base.csv_to_base(player[1], player[i], player[i+1], player[i+2], player[i+3])
                        # print x
                        base = Base(x[0], x[1], x[2], x[3], x[4])
                        base_list.append(base)
        return base_list

    @classmethod
    def csv_to_base(self, ownerStr, nameStr, attackStr, defenseStr, coordsStr):
        owner = ownerStr
        name = nameStr
        if attackStr != '':
            attack = int(attackStr)
        else:
            attack = 0
        if defenseStr != '':
            defense = int(defenseStr)
        else:
            defense = 0
        coords = (int(coordsStr[0:3]), int(coordsStr[4:7]))
        return (owner, name, attack, defense, coords)

    def coords_link(self):
        link = "[coords]{0}:{1}[/coords]".format(
            self.coords[0], self.coords[1])
        return link

    def owner_link(self):
        link = "[player]{0}[/player]".format(self.owner)
        return link

    def print_csv(self):
        print("{0},{1},{2},{3},{4}".format(
            self.owner, self.name, self.attack, self.defense, self.coords))

    def print_table(self):
        print("{0:17} {1:20} {2:3} {3:3} {4}".format(
            self.owner, self.name, self.attack, self.defense, self.coords))

