'''
fter decades of shadowy demonstrations and delays from the game’s maker, Chess 2 has finally been released. You waited in line all night to be one of the first to purchase an example of the hot sequel to the classic original, and now you are finally getting a chance to open up your new investment and take a look inside. What you find is slightly puzzling; in addition to the traditional pieces, the game has been expanded to contain a number of pieces that are not actually original.
The best-known piece that has been added to the game is the nightrider. The nightrider can make any number of knight moves in a single direction, i.e., its offset from its initial position will be 2*m in one dimension and m in the other for some nonzero integer m. Like other “sliding” pieces, if one of the knight moves would cause it to take another piece it is not able to traverse beyond that point

The archbishop is also part of Chess 2. The archbishop can simply make any move that a knight or bishop could legally make.

The strangest new piece is the kraken. The kraken can move to any square on the board, regardless of the position of any other pieces, including its own current position.

You don’t feel like reading the manual to learn about how the new pieces fit into the standard chess opening positions, so instead you place some of the pieces randomly on the board. The game you’ve decided to play is simply to count how many pieces on the board are currently being threatened. A piece is threatened if another piece is able to move into its cell and take it (note that if the kraken moves into its own cell it does not take itself).

Input
Your input file will consist of a single integer N followed by N test cases. Each case will consist of, all separated by whitespace, an integer P followed by the identities and positions of P Chess 2 pieces. Pieces are described by a single character C to denote their type (see specification below) followed by two integers R and F, the 1-based rank and file, respectively, of the piece.

You’ve decided to ignore the colors of the pieces in this game. The color of the pieces will not be reflected in the input and so cannot affect your output.

To make room for the new pieces, the Chess 2 board is a 16 by 16 grid. No specified pieces will fall outside the board, and no two pieces will occupy the same position.

The types of pieces will be specified as follows, and no entries not present in this table will appear on the board:
Piece – Abbreviation
King – K
Queen – Q
Rook – R
Bishop – B
Knight – N
Nightrider – S
Archbishop – A
Kraken – E

Output
Output a single integer, the number of threatened pieces on the board, for each test case separated by whitespace.

Constraints
N = 20
3 <= P <= 64
1 <= R, F <= 16
C will be one of K, Q, R, B, N, S, A or E

Example input
5
4 Q 1 1 B 3 1 B 5 1 B 1 4
3 S 1 1 K 2 3 S 3 5
4 N 1 1 B 3 3 Q 5 5 N 4 1
5 R 2 2 N 1 2 N 2 1 N 16 2 N 2 16
6 Q 1 1 Q 2 3 Q 3 5 Q 4 2 Q 5 4 E 1 5

Example output
2
1
3
4
6
'''
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
