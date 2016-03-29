

class Node(object):

    def __init__(self,name='anon',id=-1):
        self.name = name
        self.id = id
        self.connections = set()

    def addconnection(self,n):
        self.connections.add(n)
