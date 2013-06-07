#!/usr/bin/python

""" smallworld """
import sys
import numpy

class Person():
    
    def __init__(self, name, lat, long):
        self.name = int(name)
        self.lat = float(lat)
        self.long = float(long)
        self.closest = [(-1, float("infinity"))]*3
        self.maxdist = float("infinity")
        
    def add_neighbour(self, p):
        d = dist(p, self)
        for i in range(3):
            #print self.closest
            if (self.closest[i][1] >= d):
                self.closest.insert(i, (p,d))
                #if (i == 2):
                    #self.maxdist = d#max(d, self.maxdist)
                break
        # Delete the last one
        self.closest.pop()
        self.maxdist = self.closest[-1][1]
        return self.maxdist
        

    def __str__(self):
        return  "<Person: " + str((self.name, self.lat, self.long)) + '>'

def dist(p1, p2):
    return numpy.sqrt((p1.lat - p2.lat)**2 + (p1.long - p2.long)**2)
    
def hdist(p1,p2):
    return numpy.absolute(p1.long - p2.long)

def smallworld(filename):
    # can assume at least 4 people
    file = open(filename)
    people = map(lambda x: Person(*x.split()), file.readlines())
    people.sort(key=lambda x: x.long)
    numpeople = len(people)
    for n,p in enumerate(people):
        i = 1
        maxdist = p.maxdist
        r_looking, l_looking = True, True
        
        while ((r_looking is True) or (l_looking is True)):
            if ((n+ i < numpeople) and (r_looking is True)):
                pr = people[n+i]                
                dr = dist(p,pr)
                if (dr < maxdist):
                    maxdist = p.add_neighbour(pr)
                if(hdist(p,pr) > maxdist):
                    r_looking=False
            else:
                r_looking=False

            if ((n-i >= 0 )and (l_looking is True)):
                pl = people[n-i]
                dl = dist(p,pl)
                if (dl < maxdist):
                    maxdist = p.add_neighbour(pl)
                if(hdist(p,pl) > maxdist):
                    l_looking=False
            else:
                l_looking=False
            
            i+=1
        
    people.sort(key=lambda x: (x.name))
    for p in people:
    #    print p.name
    #    print p.closest
    #    print ""
        #print p.closest
        #print tuple(map(lambda x: x[0].name, p.closest))
        print p.name,
        print '%d,%d,%d' % tuple(map(lambda x: x[0].name, p.closest))
    
        
    return

def smallworld2(filename):
    # can assume at least 4 people
    file = open(filename)
    people = map(lambda x: Person(*x.split()), file.readlines())
    people.sort(key=lambda x: x.long)
    
    unsure = []
    for p in people:
        unsure = filter(lambda u: friendless(p,u), unsure)
        unsure.append(p)

    unsure = []
    people.sort(key=lambda x: x.long, reverse=True)

    for p in people:
        unsure = filter(lambda u: friendless(p,u), unsure)
        unsure.append(p)
        
    people.sort(key=lambda x: (x.name))
    for p in people:
        print p.name,
        print '%d,%d,%d' % tuple(map(lambda x: x[0].name, p.closest))    
    return

def friendless(p, u):
    """Updates u and p if they are close enough to be friends. Returns False if u has found closest friends"""
    d = dist(p,u)
    maxdist = u.maxdist
    if (d < maxdist):
        maxdist = u.add_neighbour(p)
    #if (d < p.maxdist):
    #    p.add_neighbour(u)
    if (hdist(p,u) >= maxdist):
        return False
    else: return True
    
    

    
def smallworld1(filename):
    file = open(filename)
    people = map(lambda x: Person(*x.split()), file.readlines())
    
    npeople = len(people)
    distances = numpy.zeros((npeople, npeople))
    for i in range(npeople):
        for j in range(npeople):
            distances[i,j] = dist(people[i], people[j])

    # Now find the closest friends
    for p in people:
        p.closest = nargmin(distances[p.name-1, :],4)
        
    for p in people:
        print '%d %d,%d,%d' % tuple(map(lambda x: x[1] +1, p.closest))
    
    #print_graphics(people)
    file.close()
    return

def print_graphics(people):
    array = numpy.zeros((36, 18))
    for p in people:
        array[int(p.long/10)+18,int(p.lat/10) +9] = p.name
    
    print array
def nargmin(array, n):
    """Takes an array and returns the indexes of rthe n minimum elements in order"""
    topfriends = [(array[i], i) for i in range(n)]
    topfriends.sort()
    for j in range(n, array.size):
        i = 0
        for i in range(n):
            if (topfriends[i][0] > array[j]):
                topfriends.insert(i, (array[j], j))
                break
        topfriends = topfriends[:n]
        
    return topfriends
    
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) != 2):
        sys.exit("Usage: smallworld inputfile")
    smallworld((sys.argv[1]))
