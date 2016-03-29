import csv

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

    def addowner(self, owner_id):
        self.owners.add(owner_id)
        self.check_found()

    def addcat(self, cat_id):
        self.cats.add(cat_id)
        self.check_found()

    def check_found(self):
        found_set = self.cats.intersection(self.owners)
        if found_set:
            self.cats = self.cats.difference(found_set)
            self.owners = self.owners.difference(found_set)
            self.open = False
            self.log_finds(found_set=found_set)
            self.outputfinds()

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