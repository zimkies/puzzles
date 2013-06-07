#!/usr/bin/python

# Note that one enterpretation of the question may mean the graph is unconnected
# In that case, I need to add code to search each component and then check if
# a solution exists such that any combination of components adds to the same answer.

""" sophie """
import sys

class Spot():
    
    def __init__(self, location, neighbours, probability):
        self.loc =  location
        self.neighbours = neighbours
        self.prob = float(probability)
        
class Path():
    
    def __init__(self, source, dest, time):
        self.source = source
        self.dest = dest
        self.time = int(time)

def sophie(filename):
    """Prints the number of liars and honest people in decreasing sorted order"""
    file = open(filename)
    n = int(file.readline())
    if (n == 0):
        # Need to change that
        sys.exit("0")
    
    # The graph
    home = {}
    
    # Collect locations
    for i in range(n):
        location, probability = file.readline().strip().split()
        neighbours = set([])
        home[location] = Spot(location, neighbours, probability)
        if (i == 0):
            start = location
        
    
    c = int(file.readline())
    for e in range(c):
        path = Path(*file.readline().split())
        home[path.source].neighbours.add(path)
    
    # Make the graph into an undirected graph
    complete_graph(home)
    
    # Do a BFS to make sure that the graph is connected:
    if (bfs_count(home, start) != n):
        print "-1.00"
        sys.exit()

def complete_graph(graph):
    """ Takes a directed graph and turns it into a undirected graph"""
    for k in graph.keys():
        for v in graph[k].neighbours:
            graph[v.dest].neighbours.add(Path(v.dest, v.source, v.time))

class BFS_wrapper():
    
    def __init__(self, item):
        self.item = item
        self.visited = 0

def bfs_count(graph, start):
    # Do a BFS
    newgraph = {}
    for k in graph.keys():
        newgraph[k] = BFS_wrapper(graph[k])
    
    stack = []
    p = newgraph[start]
    p.visited = 1
    stack.append(p)
    count = 1
    
    while (len(stack) > 0):
        p = stack.pop()

        # add the children to the stack
        for child in p.item.neighbours:
            c = newgraph[child.dest]
            if (c.visited == 0):
                c.visited = 1
                count += 1
                stack.append(c)
    return count

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: ./sophie inputfile")
    sophie(sys.argv[1])