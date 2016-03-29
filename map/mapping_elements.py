import csv

class Node(object):
    """
    A map node
    """

    def __init__(self,name='anon', id=-1):
        self.name = name
        self.id = id
        self.connections = set()

    def addconnection(self,n):
        """
        :param n: integer id of station connected to
        Connections are uni-directional
        """
        self.connections.add(n)


def read_datafile(fn):
    """
    Step through the CSV data file & generate each row
    :param fn: filename of source
    :return: yields each row as a list
    """
    with open(fn, 'rb') as csvfile:
        nodereader = csv.reader(csvfile, delimiter=',')
        for row in nodereader:
            yield row