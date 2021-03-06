#!/usr/bin/python

""" swarm """
import sys
import math

class Base():
    
    def __init__(self, strength, minerals, id):
        self.strength = int(strength)
        self.minerals = int(minerals)
        self.id = int(id)
        self.attackers = min_n_towin(self.minerals, self.strength)
        self.booty = expectedbooty(self.minerals, self.attackers, self.strength)

    def __str__(self):
        return  "<Base: " + str((self.strength, self.minerals)) + '>'
        
class Planet():
    
    def __init__(self, bases, zergs):
        self.nbases = len(bases)
        self.nzergs = int(zergs)
        self.bases = bases

def winchance(z, s):
    #P(z,s) = e^(-63s+10)/
    #(e^(-63s+10)+e^(-21z))
    num = -63*s + 10 + 21*z
    if (num < -1000):
        return 0.0
    elif (num > 100):
        return 1.0
    else:
        exp = math.e**num
        return exp/(exp + 1)
        
def min_n_towin(m,s):
    num = (math.log(2*m) -63*s + 10)/-21.
    return int(math.ceil(num))
    
def expectedbooty(m,z,s):
    return int(round(winchance(z,s)*m))

def swarm(filename, option=0):
    
    file = open(filename)
    nPlanets = int(file.readline())
    for n in range(nPlanets):
        t, z = map(int, file.readline().split())
        bases = []
        for b in range(t):
            base = Base(*file.readline().split(), id=b)
            bases.append(base)
        planet = Planet(bases, z)
        
        if (option==0):
            strategy = Strategy(planet)
            best = strategy.optimum()
            print best.attackers, best.booty
            for b in best.used:
                print b.id, b.attackers,
            print ""
        elif (option==1):
            strategy = Strategy1(planet)
            strategy.calculate_optimum()
            print strategy.bestzergsused, strategy.bestscore
            usedbases = filter(lambda x: (x[1] == 1),zip(strategy.bases, strategy.beststrategy))
            for b in usedbases:
                print b[0].id, b[0].attackers,
            print ""

class Strategy:
    def __init__(self, planet):
        # filter out bases which are definitely not viable:
        self.z = planet.nzergs
        self.bases = filter(lambda b: (b.attackers <= planet.nzergs), planet.bases)
        self.bases.sort(key=lambda x: x.attackers)
        self.nbases = len(self.bases)
        self.strategy = [None]*(self.z +1)
        self.strategy[0] = SubStrategy([], self.bases[:], 0, 0)
        
    def optimum(self):
        for i in range(self.z):
            ss = self.strategy[i]
            if (ss is not None):
                for bi, b in enumerate(ss.unused):
                    n = b.attackers + i # new strategy index
                    if (n <= self.z):
                        nss = self.strategy[n]
                        used = ss.used[:]
                        used.append(b)
                        unused = ss.unused[:]
                        unused.pop(bi)
                        attackers = n
                        booty = ss.booty + b.booty
                        if (nss is None):
                            self.strategy[n] = SubStrategy(used, unused, attackers, booty)
                        elif (nss.booty < ss.booty + b.booty):
                            # Update the substrategy
                            nss.unused = unused
                            nss.used = used
                            nss.attackers = attackers
                            nss.booty = booty
                    else:
                        break
            
        #best = max(self.strategy, key=lambda x: x.booty)
        best = self.strategy[0]
        for b in self.strategy:
            if b is not None:
                if (b.booty > best.booty):
                    best = b
        
        best.used.sort(key=lambda x: x.id)
        return best

class SubStrategy():
    """Storage Class for a substrategy"""
    def __init__(self, used, unused, attackers, booty):
        self.used = used
        self.unused = unused
        self.attackers = attackers
        self.booty = booty
    
class Strategy1:
    
    def __init__(self, planet):
        # filter out bases which are definitely not viable:
        self.bases = filter(lambda b: (b.attackers <= planet.nzergs), planet.bases)
        self.nbases = len(self.bases)
        self.strategy = [0]*len(self.bases)
        self.z = planet.nzergs
        self.bestscore = 0
        self.bestzergsused = 0
        self.beststrategy = self.strategy[:]
        
    def optimum(self, index):
        if (index >= self.nbases):
            #print self.strategy 
            total_attackers = reduce(lambda t, b: t + b[0]*b[1].attackers, zip(self.strategy, self.bases), 0)
            if (total_attackers <= self.z):
                score = reduce(lambda t, b: t + b[0]*b[1].booty, zip(self.strategy, self.bases),0)
                if (score > self.bestscore):
                    self.bestscore = score
                    self.beststrategy = self.strategy[:]
                    self.bestzergsused = total_attackers
        
        else:
            for i in range(2):
                self.strategy[index] = i
                self.optimum(index+1)
                
            self.strategy[index] = 0
    
    def calculate_optimum(self):
        self.optimum(0)
        
    
    
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: swarm inputfile option")
    
    # Which option?
    option = 0
    if (len(sys.argv) == 3):
        if (sys.argv[2] == '1'):
            option = 1
    swarm(sys.argv[1], option)

