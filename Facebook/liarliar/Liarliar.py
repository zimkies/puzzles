#!/usr/bin/python

""" Liarliar """
import sys

class Person():
    
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours
        self.honesty = 0

def liars(filename):
    """Prints the number of liars and honest people in decreasing sorted order"""
    file = open(filename)
    n = int(file.readline())
    
    # The graph
    people = {}
    
    # Collect data and form graph
    for i in range(n):
        accuser, j = file.readline().strip().split()
        accused = set([])
        for p in range(int(j)):
            accused.add(file.readline().strip())
        people[accuser] = Person(accuser, accused)

    # Make the graph into an undirected graph
    complete_graph(people)
    
    # Do a DFS    
    stack = []
    p = people[people.keys()[0]]
    p.honesty = 1
    stack.append(p)
    honest, liar = 0,0
    
    while (len(stack) > 0):
        p = stack.pop()

        # add the children to the stack
        for child in p.neighbours:
            c = people[child]
            if (c.honesty == 0):
                c.honesty = p.honesty*-1
                if (c.honesty >0):
                    honest += 1
                else:
                    liar += 1
                stack.append(c)
    
    # Return a sorted answer
    answer = [honest, liar]
    answer.sort()
    file.close()
    print answer[0], answer[1]
        
def complete_graph(graph):
    """ Takes a directed graph and turns it into a undirected graph"""
    for k in graph.keys():
        for v in graph[k].neighbours:
            graph[v].neighbours.add(k)
            

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: Python Liarliar inputfile")
    liars(sys.argv[1])