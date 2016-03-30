import csv
import random

class Station(object):

    def __init__(self, parent=None):
        self.owners = set()
        self.cats = set()
        self.open = True
        self.parent = parent
        self.findlog = []

    @property
    def closed(self):
        return not self.open

    def addowner(self, owner):
        self.owners.add(owner)
        self.check_found()

    def remove_owner(self, owner):
        self.owners.remove(owner)

    def remove_cat(self, cat):
        self.cats.remove(cat)

    def addcat(self, cat):
        self.cats.add(cat)
        self.check_found()

    def check_found(self):
        cat_ids = {item.id for item in self.cats}
        owner_ids = {item.id for item in self.owners}
        found_set = cat_ids.intersection(owner_ids)
        if found_set:
            self.cats = self.cats.difference(found_set)
            self.owners = self.owners.difference(found_set)
            self.open = False
            self.log_finds(found_set=found_set)
            self.outputfinds()
            for cat in self.cats.copy():
                if cat.id in found_set:
                    self.cats.remove(cat)
            for owner in self.owners.copy():
                if owner.id in found_set:
                    self.owners.remove(owner)


    def log_finds(self,found_set):
        self.findlog = []
        for id in found_set:
            if self.parent:
                station_msg = " - {station} is now closed".format(station=self.parent.name)
            else:
                station_msg = ''
            self.findlog.append("Owner {id} found cat {id}{station_msg}".format(id=id,station_msg=station_msg))
    def outputfinds(self):
        for find in self.findlog:
            print find

class Node(object):
    """
    A map node
    """
    occupiers = None

    def __init__(self,name='anon', id=-1):
        self.name = name
        self.id = int(id)
        self.connections = set()
        self.occupiers = Station(self)

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def addconnection(self,n):
        """
        :param n: integer id of station connected to
        Connections are uni-directional
        """
        self.connections.add(n)

class Graph(object):

    def __init__(self):
        self.nodes = {}

    def readnodefile(self, fn):
        for [node_id, node_name] in read_datafile(fn):
            self.nodes[int(node_id)] = Node(name=node_name, id=int(node_id))

    def readconnections(self, fn):
        for [from_id, to_id] in read_datafile(fn):
            self.nodes[int(from_id)].addconnection(int(to_id))
            self.nodes[int(to_id)].addconnection(int(from_id))

class Player(object):

    def __init__(self,id=0):
        self.id = id

    def move(self, destinations, seed=None):
        raise NotImplementedError()

    def __repr__(self):
        return '{} : id {}'.format(self.__class__.__name__ ,self.id)

class Cat(Player):
    def move(self, destinations, seed=None):
        possible_destinations = set(destinations)
        if seed is not None:
            random.seed(seed)
        try:
            new_destination = random.choice(list(possible_destinations))
            return new_destination
        except IndexError:
            return None


class Owner(Player):

    visited = set()

    def move(self,destinations, seed=None):
        possible_destinations = set(destinations)
        possible_destinations = possible_destinations.difference(self.visited)
        # only backtrack if there's no alternative
        if len(possible_destinations) == 0:
            possible_destinations = set(destinations)
        if seed is not None:
            random.seed(seed)
        try:
            new_destination = random.choice(list(possible_destinations))
            self.visited.add(new_destination)
            return new_destination
        except IndexError:
            return None


def read_datafile(fn, delimiter=','):
    """
    Step through the CSV data file & generate each row
    :rtype: generator
    :param fn: filename of source
    :return: yields each row as a list
    """
    with open(fn, 'rb') as csvfile:
        nodereader = csv.reader(csvfile, delimiter=delimiter)
        for row in nodereader:
            yield row