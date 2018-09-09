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
    
    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self.graph and node2 in self.graph[node1]
    
    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for node in self.graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None
    
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

    def check(self):
    	for n,k in self.graph.items():
    		print(n,'--->',k)
    	print(self.graph['B'])
        
    def BFS(self,s):
    	visited=[False]*(len(self.graph))
    	queue=deque()
    	queue.append(s)
    	visited[s]=True

    	while queue:
    		s=queue.popleft()
    		print(s,end="-->")

    		for nodes in self.graph[s]:
    			#print(nodes,'no')
    			if(visited[nodes]==False):
    				queue.append(nodes)
    				visited[nodes]=True
    
    def DFS(self,s):
	    visited=[False]*(len(self.graph))
	    for i in range(len(self.graph)):
	    	if(visited[i]==False):
	    		self.DFS_track(i,visited)

    def DFS_track(self,s,visited):
        visited[s]=True
        print(s,end="-->")

        for nodes in self.graph[s]:
        	if(visited[nodes]==False):
        		visited[nodes]=True
        		self.DFS_track(nodes,visited)
