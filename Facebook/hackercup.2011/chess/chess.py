import sys
import numpy

class Piece():
    def __init__(piece,n,pos):
        piece.name = n
        piece.pos = pos
        piece.r = pos[0]
        piece.c = pos[1]
        piece.threats = 0
class Chess():
    
    def __init__(self, input):
        self.board = numpy.zeros((17,17), 'str')
        self.npieces = int(input[0])
        self.pieces = {}
        
        for i in range(1, len(input), 3):
            
            p = Piece(input[i],(int(input[i+1]),int(input[i+2])))
            self.pieces[p.pos] = p
            self.board[p.pos] = p.name
            
    def printer(self):
        print self.board
    
    def getthreats(self):
        threats = 0
        for k,v in self.pieces.items():
            movelist = moves(v.name, v.pos)
            for p in movelist:
                space = self.board[p]
                if (space != ''):
                    print v.name, p
                    self.pieces[p].threats +=1
        
        for k,v in self.pieces.items():
            if (v.threats >= 1):
                print v.pos, v.threats, v.name
                threats += 1
        return threats
    
    
        
    
def moves(piece, pos):
    movelist = []
    r,c = pos
    if (piece == 'K'):
        if (inbounds(r-1, c-1)):
            movelist.append((r-1, c-1))
        if (inbounds(r-1, c)):
            movelist.append((r-1, c))
        if (inbounds(r-1, c+1)):
            movelist.append((r-1, c+1))
        
        if (inbounds(r, c-1)):
            movelist.append((r, c-1))
        if (inbounds(r, c+1)):
            movelist.append((r, c+1))
            
        if (inbounds(r+1, c-1)):
            movelist.append((r+1, c-1))
        if (inbounds(r+1, c)):
            movelist.append((r+1, c))
        if (inbounds(r+1, c+1)):
            movelist.append((r+1, c+1))
    
    elif (piece == 'Q'):
        s = set(moves('R', pos))
        s2 = set(moves('B', pos))
        s = s.union(s2)
        movelist.extend(list(s))
     
    elif (piece == "R"):
        for i in range(1,17):
            if (i != r):
                if (inbounds(i, c)):
                    movelist.append((i,c))
        for i in range(1,17):
            if (i != c):
                if (inbounds(r,i)):
                    movelist.append((r,i))
                    
    elif (piece == "B"):
        ru,rd = r,r
        column = c
        for i in range(1,17):
            if (inbounds(ru,c-i)):
                movelist.append((ru,c-i))
            if (inbounds(rd,c-i)):
                movelist.append((rd,c-i))
            if (inbounds(rd,c+i)):
                movelist.append((rd,c+i))
            if (inbounds(ru,c+i)):
                movelist.append((ru,c+i))
                
    elif (piece == "N"):
        movelist.extend(knightmoves(pos))
        
    
    elif (piece == "S"):
        movelist.extend(knightmoves(pos,9))
        print movelist
    
    elif (piece == "A"):
        s = set(moves('B', pos))
        s2 = set(moves('N', pos))
        s = s.union(s2)
        movelist.extend(list(s))
    
    elif (piece == "E"):
        for i in range(1,17):
            for j in range(1,17):
                if ((i,j) != pos):
                    movelist.append((i,j))
    
    return movelist
                    
    
def knightmoves(pos, rang=2):
    movelist = []
    r,c = pos
    for i in range(1,rang):
        j = 2*i
        if (inbounds(r+j,c+i)):
            movelist.append((r+j,c+i))
        if (inbounds(r+j,c-i)):
            movelist.append((r+j,c-i))
        if (inbounds(r+i,c+j)):
            movelist.append((r+i,c+j))
        if (inbounds(r-i,c+j)):
            movelist.append((r-i,c+j))
        if (inbounds(r-j,c+i)):
            movelist.append((r-j,c+i))
        if (inbounds(r-j,c-i)):
            movelist.append((r-j,c-i))
        if (inbounds(r+i,c-j)):
            movelist.append((r+i,c-j))
        if (inbounds(r-i,c-j)):
            movelist.append((r-i,c-j))
    
    return movelist
            
def inbounds(*pos):
    r,c = pos
    if r not in range(1, 16+1):
        return False
    elif c not in range(1, 16+1):
        return False
    return True

def chess(filename):
    
    f = open(filename)
    t = int(f.readline())
    for i in range(t):
        line = f.readline().split()
        c = Chess(line)
        c.printer()
        print c.getthreats()
        #for j in range(int(nums[0])):
        #    nums.append(f.readline().split()[0])
        ##f.readline()
        #nums.append(string)
        #print nums
       # map = Map(nums)
        #map.print_maze()
        ##ath = dijkstras.shortestPath(map.graph, map.start, map.end)
        
if __name__ == "__main__":
    # Usage
    if (len(sys.argv) > 3):
        sys.exit("Usage: round1 nputfile option")
    
    # Which option?
    chess(sys.argv[1])