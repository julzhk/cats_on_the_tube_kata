import csv

class Node(object):
    """
    A map node
    """

    def __init__(self,name='anon', id=-1):
        self.name = name
        self.id = int(id)
        self.connections = set()

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
        self.nodes = []

    def readnodefile(self,fn):
        for row in read_datafile(fn):
            self.nodes.append(Node(name=row[1],id=row[0]))


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