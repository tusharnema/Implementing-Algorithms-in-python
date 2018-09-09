from collections import defaultdict
from collections import deque

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)
    
    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)
            
    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)
    
    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self.graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self.graph[node]
        except KeyError:
            pass
