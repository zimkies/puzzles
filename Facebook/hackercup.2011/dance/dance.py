
import sys
import math
import numpy
import dijkstras


class Map():
    
    def __init__(self, rep):
        self.r = int(rep[0])
        self.c = int(rep[1])
        self.colours = {}
        string = rep[2:]
        self.maze = numpy.zeros((self.r, self.c), 'str')
        self.make_maze(string)
        
    def print_maze(self):
        print self.maze
    
    def make_maze(self, string):
        for i in range(self.r):
            self.process(string, i)
        
        for colour in map(lambda x: str(x), range(1,10)):
            self.colours[colour] = []
        for i in range(self.r):
            for j in range(self.c):
                # Get start
                colour = self.maze[i,j]
                if (colour == 'S'):
                    self.start = (i,j)
                    
                # Get End   
                elif (colour == 'E'):
                    self.end = (i,j)
        
                # Get colours
                elif (colour in map(lambda x: str(x), range(1,10))):
        
                    self.colours[colour].append((i,j))
                
        
                
    def process(self, string, i):
        self.maze[i,:] = list(string[i])
        
    def make_graph(self):
        self.graph = {}
        for i in range(self.r):
            for j in range(self.c):
                neighbours = []
                #TOP
                if (i != 0):
                    neighbours.append(((i-1, j), self.distance((i,j), (i-1,j))))
                
                #Bottom
                if (i != self.r-1):
                    neighbours.append(((i+1, j), self.distance((i,j), (i+1,j))))
                
                #left
                if (j != 0):
                    neighbours.append(((i, j-1), self.distance((i,j), (i,j-1))))
                # right
                if (j != self.c-1):
                    neighbours.append(((i, j+1), self.distance((i,j), (i,j+1))))
                
                # colour
                colour = self.maze[i,j]
                if (colour in map(lambda x: str(x), range(1,10))):
                    for place in self.colours[colour]:
                        neighbours.append((place, 1))
                        
                self.graph[(i,j)] = dict(neighbours)
                
    # The distance between two places
    def distance(self, a, b):
        if (self.maze[b] == "W"):
            return float("inf")
        else:
            return 1
        
def dance(filename):
    
    f = open(filename)
    n = int(f.readline())
    for i in range(n):
        #print i
        fff = f.readline()
        nums  =fff.split()
        string = ' '
        for j in range(int(nums[0])):
            nums.append(f.readline().split()[0])
        f.readline()
        #nums.append(string)
        #print nums
        map = Map(nums)
        #map.print_maze()
        map.make_graph()
        path = dijkstras.shortestPath(map.graph, map.start, map.end)
        print len(path) - 1

if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    # Which option?
    dance(sys.argv[1])