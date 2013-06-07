import numpy as np
def p1(up=1000):
    r = range(1,up)
    r = filter(lambda(x):((x%3==0) or (x%5 == 0)), r)
    print sum(r)
    
def p2(x=4000000):
    r = fib(x)
    r = filter(lambda(y): (y%2 == 0), r)
    return sum(r)
    
def fib(x):
    
    if (x < 0):
        return []
    if (x == 1):
        return [1]
        
    list = [1,2]
    while(list[-1]+list[-2] <= x):
        list.append(list[-1]+list[-2])       
    return list

def p3(x=600851475143):
    rep = [(1,1)]
    prime = 2
    
    while(x!=1):
        if (x%prime==0):
            x = x/prime
            if (prime == rep[-1][0]): 
                rep[-1] = (rep[-1][0],rep[-1][1]+1)
            else:
                rep.append((prime, 1))
        else:
            prime = prime +1
            
    return rep, rep[-1][0]
    


def p4(z=1000):
    r = range(2*z - 1)
    r.reverse()
    r = map(lambda(x): x/2., r)
    
    for i in r:
        x,y = int(i),int(i+.5)
        while (y<=z-1 and x>=0):
            if (ispalindrome(x*y)):
                return (x,y, x*y)
            else:
                x,y = x-1, y+1
    return None
    
def ispalindrome(x):
    x = str(x)
    for i in range(len(x)/2):
        if(x[i] != x[-(i+1)]):
            return False
    return True
    

def p5(z=20):
    l = 1
    for i in map(lambda(x): x+1, range(z)):
        l = LCM(l, i)
    return l

def LCM(a,b):
    l = a
    while (l%b != 0):
        l = l+a
    return l

def p6(x=100):
    r=range(1,x+1)
    s = ((1+x)*x)/2
    s2 = s**2
    r2 = sum(map(lambda(x): x**2, range(1,x+1)))
    return r2 -s2

def p7(x=10001):
    maxindex = 2**20
    y = 4
    p = primes(y)
    l = len(p)
    while (l < x):
        if (l>maxindex):
            raise Exception("maxindex exceeded")
        print "got " + str(l) +" primes"
        y=y*2
        p = primes(y, p)
        l = len(p)
        
    return p, p[x-1], l
    
def primes(x, p=[2]):
    if (x< 8):
        print "argument x must be at least 8"
        return p
    s = p[-1]
    r = [0]*(x-s)
    # update for primes already known
    for i in p:
        if (i > 1):
            for j in range(s + (i-s%i), x, i):
                r[j-s-1] = -1
    
    for i in range(p[-1]+1,x):
        if (r[i-s-1] != -1):
            p.append(i)
            for j in range(i, x, i):
                r[j-s-1] = -1
                
    return p

p8string = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace('\n', "")


def p8(string=p8string, size=5):
    maxprod = 1
    for i in range(len(string) - size+1):
        ministr = string[i:i+size]
        prod  =1
        for d in ministr:
            prod = prod*int(d)
        if (prod > maxprod):
            maxprod = prod
    return maxprod

def p9(x=1000):
    r = range(1,x)
    r.reverse()
    for c in r:
        c2 = c**2
        for a in range(1,c):
            #print c, a,np.sqrt(c2 - a**2),x- a-c
            b=x-a-c
            if (b>0):
                if (np.sqrt(c2 - a**2) == b):
                    return a,b,c,a*b*c
    return None

def p10(x=2000000):
    return sum(primes(x))
    

p11string  = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

def p11(string=p11string):
    size =4
    a = string.splitlines()
    for i,s in enumerate(a):
        a[i] = map(lambda(x): int(x), s.split(" "))
    a = np.array(a)
    dim = a.shape[0]
    maxprod =1
    temp1 = np.zeros(size)
    temp2 = np.zeros(size)
    for i in range(dim - size+1):
        for j in range(dim - size+1):
            product1 = np.prod(a[i:i+size,j])
            product2 = np.prod(a[j,i:i+size])
            maxprod = max(product1, product2, maxprod)
            
            for k in range(size):
                temp1[k] = a[i + k, j+k]
                temp2[k] = a[dim -(i + k+1), j+k]
                
            product1 = np.prod(temp1)
            product2 = np.prod(temp2)
            maxprod = max(product1, product2, maxprod)
    
    return maxprod
    
def p12(x=500):
    #maxindex = 2**20
    #y =1
    #t = triangle2(y)
    #l = len(divisors(t[-1][0]))
    #y=y*2
    #while (l <= x):
    #    t = triangle2(y, t[-1])
    #    l = len(divisors(t[-1][0]))
    #    #for i in range(y, y*2):
    #    #    t = triangle2(y, t[-1])
    #    #    print t
    #    #    l = len(divisors(t[-1][0]))
    #    #    #print "triangle number: "+ str(i)
    #    #    #print "triangle: " + str(t)
    #    #    #print "divisors: " + str(l)
    #    y=y*2
    #for (n,i) in t:
    #    if len(divisors(n)) > x:
    #        return t,(n,i), divisors(n)
    #return None
    maxindex = 2**20
    y =1
    t = triangle2(y)
    l = len(divisors(t[-1][0]))
    y=y*2
    while (y< maxindex):
        for n,i in t:
            l = len(divisors(n))
            if l > x:
                return (n,i), divisors(n)
        t = triangle2(y, t[-1])
        y=y*2
    return None



def triangle2(x, last = (0,0)):
    """Returns a list of tuples (triangle, index) including the index last[1] up to x"""
    if (x <= last[1]):
        return None
    list = [last]
    for i in range(last[1]+1, x+1):
        list.append((i+list[-1][0], i))
    return list[1:]

def triangle(x, last = 1):
    if (x == 1):
        return last
    t = last
    for i in range(last+1, x+1):
        t = i+t
    return t
    
def triangles(x, list=[1]):
    l = len(list)
    if (x <= l):
        return list[:x]
    for i in range(l+1, x+1):
        list.append(i+list[-1])
    return list

def divisors(x):
    if (x==1):
        return [1]
    l = []
    sqr = int(np.sqrt(x))
    for i in range(1,sqr+1):
        if (x%i==0):
            l.append(i)
            j = x/i
            if (j!=i):
                l.append(x/i)
    return l
    
    
p13string = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
def p13(x=10, string=p13string):
    string = string.splitlines()
    ints = np.array(map(lambda(x): int(x), string))
    print ints
    print ints[2]
    s = sum(ints)
    print s
    newstring = str(s)
    return newstring[:x]
    
def p14(x=1000000):
    d = p14dict()
    
    lmax = (1,1)
    for i in range(1,x):
        l = d.slength(i)
        lmax = max((l,i), lmax)
    
    return lmax
   
class p14dict():
    def __init__(self):
        self.dict = {1: 1}
        
    def slength(self, n):
        if (n in self.dict):
            return self.dict[n]
        else:
            n1 = p14mapper(n)
            len = self.slength(n1)+1
            self.dict[n] = len
            return len

def p14mapper(n):
    if (n%2==0):
        return n/2
    else:
        return 3*n+1

def p15(x=20,y=20):
    npaths = p15store(x,y)

    p = npaths.paths(0,0)
    print npaths.s
    return p
    
class p15store():
    def __init__(self, v=21,h=21):
        self.s = np.zeros((v,h))
        self.s[v-1,h-1] = 1
        self.h=h
        self.v=v
    
    def paths(self,x,y):
        if (self.s[x,y] > 0):
            return self.s[x,y]
        else:
            vpath,hpath =0,0
            if (x < self.v-1):
                vpath = self.paths(x+1, y)
            if (y < self.h-1):
                hpath = self.paths(x, y+1)
            self.s[x,y] = vpath+hpath
            return self.s[x,y]
            
def p16(p):
    s = 2**p
    a = np.array(map(lambda(x): int(x), str(s)))
    print a
    return sum(a)
    
    
def p17(x=1000):

    nums = []  
    for n in range(x+1):
        nums.append(int2words(n))
    
    string = "".join(nums)
    string = string.replace(" ", "")
    
    return nums, string, len(string)
    
def int2words(number):
    if (number ==1000):
        return " one thousand"
    
    ones = {0: "", 1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9: "nine"}
    tens= {0: "", 1: "ten", 2: "twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9: "ninety"}
    teens= {0: "ten", 1: "eleven", 2: "twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9: "nineteen"}
    
    l =""
    s = str(number)
    length = len(s)

    hundredsb = False # a hundred is present
    tensb = False # a ten is present
    teensb = False #a teen is present
    for i,d in enumerate(s):
        j = length-i
        # hundreds
        if (j %3 == 0):
            w = ones[int(d)]
            if (len(w) > 0):
                l = l + " " +   ones[int(d)] + " " + "hundred"
                hundredsb = True
        #tens
        elif (j %3 == 2):
            w = tens[int(d)]
                
            if (len(w) > 0):
                if (hundredsb is True):
                    l += " and "
                    tensb = True
            if (w is "ten"):
                teensb = True
            else:
                l = l + " " + w + " "
        # units
        elif (j%3== 1):
                
            w = ones[int(d)]
            if (len(w) > 0):
                if ((hundredsb is True) and (tensb is not True)):
                    l+= " and "
            
            if (teensb is True):
                l += " " + teens[int(d)] + " "
            else:
                l = l + " " + w + " "

            hundredsb = False
            teensb = False
                
    return l

#def int2words(number):
#    ones = {0: "", 1: "one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9: "nine"}
#    tens= {0: "", 1: "ten", 2: "twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9: "ninety"}
#    teens= {0: "ten", 1: "eleven", 2: "twelve", 3:"thirteen", 4:"forteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9: "nineteen"}
#    exponents = {1: "", 4: "thousand", 7:"million", 10:"billion"}
#    
#    l =""
#    s = str(number)
#    length = len(s)
#
#    hundredsb = False
#    teensb = False
#    thsnd = False
#    overhundred = False
#    for i,d in enumerate(s):
#        j = length-i
#        # hundreds
#        if (j %3 == 0):
#            w = ones[int(d)]
#            if (len(w) > 0):
#                l = l + " " +   ones[int(d)] + " " + "hundred"
#                hundredsb = True
#                overhundred = True
#                thsnd = True
#        #tens
#        elif (j %3 == 2):
#            w = tens[int(d)]
#                
#            if (len(w) > 0):
#                thsnd = True
#                if (hundredsb is True):
#                    l += " and "
#                    hundredsb = False
#            if (w is "ten"):
#                teensb = True
#            else:
#                l = l + " " + w + " "
#        # units
#        elif (j%3== 1):
#                
#            w = ones[int(d)]
#            if (len(w) > 0):
#                thsnd = True
#                if (overhundred is True and (j == 1)):
#                    l += " and "
#                elif (hundredsb is True):
#                    l+= " and "
#            
#            if (teensb is True):
#                l += " " + teens[int(d)] + " "
#            else:
#                l = l + " " + w + " "
#            
#            if (thsnd == True):
#                l += exponents[j] + " "
#            
#            thsnd = False
#            overhundred = True
#            hundredsb = False
#            teensb = False
#                
#    return l

p18string ="""
3
7 4
2 4 6
8 5 9 3"""
#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#88 02 77 73 07 63 67
#99 65 04 28 06 16 70 92
#41 41 26 56 83 40 80 70 33
#41 48 72 33 47 32 37 16 94 29
#53 71 44 65 25 43 91 52 97 51 14
#70 11 33 28 77 73 17 78 39 68 17 57
#91 71 52 38 17 14 91 43 58 50 27 29 48
#63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#"""

def p18(string=p18string):
    strarray = string.splitlines()
    strarray = filter(lambda x: (len(x) > 0), strarray)
    strarray = map(lambda x: x.split(" "), strarray)     
    triangle = np.zeros((len(strarray),len(strarray)))
    for i in range(len(strarray)):
        for j in range(i+1):
            print i, j
            triangle[i,j] = int(strarray[i][j])
    d = p18store(triangle)
    
    bestpath = d.dist(0,0)
    return d.store, bestpath
class p18store:
    
    def __init__(self, triangle):
        self.triangle = triangle
        self.store = np.zeros(triangle.shape)-1
        size = triangle.shape[0]
        self.store[size-1] = triangle[size-1]
        
    def dist(self,i,j):
        if (self.store[i,j] > -1):
            return self.store[i,j]
        l = self.dist(i+1,j)
        r = self.dist(i+1, j+1)
        d = self.triangle[i,j] + max(l,r)
        self.store[i,j] = d
        return d
    
def p19():
    x = [[31,28,31,30,31,30,31,31,30,31,30,31]]
    x.append(x[0][:])
    x[1][1] = 29
    l = [1]
    for years in range(1901, 2001):
        for month in range(12):
            if (years%4 == 0 and (years%400 ==0)):
                l.append(l[-1] + x[0][month])
            else:
                l.append(l[-1] + x[1][month])
                
    Sundays1st = filter(lambda x: (x%7 == 5), l)
    return Sundays1st, len(Sundays1st), l
    
def p20fact(x):
    if (x == 1):
        return 1
    return x*p20fact(x-1)
    
def p20(x):
    s = 0
    fact = str(p20fact(x))
    for i in fact:
        s+= int(i)
    return s, fact

def p21divisors(x):
    divisors(x)
def p21(x=10000):
    d = []
    for i in range(x):
        s = sum(filter(lambda y: (y!=i), divisors(i)))
        d.append(s)
        
    amicable = []
    for a in range(x):
        b = d[a]
        if (b<x):
            if ((a == d[b]) and (a != b)):
                amicable.append(a)
                amicable.append(b)
    
    s = sum(amicable)/2
    return amicable,d, s

def p22():
    f = open("names.txt")
    names = f.readlines()[0].replace('"',"").split(',')
    names.sort()
    return reduce(lambda psum,ni : (p22nameval(ni[0],ni[1], psum)), zip(names, range(1,len(names)+1)), 0) 
    
def p22nameval(name,index,psum):
    return (index* sum([(ord(c)-(ord('A')-1)) for c in name ])) + psum
 
   
#def p23(x=28123):
#    r = range(x+1)
#    abundants = p23store(x)
#    max = r[0]
#    mylist = []
#    for n in r:
#        if (p23abundant(n) == True):
#            abundants.add(n)
#
#    #print abundants.store
#    print mylist
#    return max,abundants.abs, sum(mylist)

def p23(x=28123):
    r = range(x+1)
    store = [False]*(x+1)
    abundants = filter(p23abundant, r)
    for i in abundants:
        for j in abundants:
            if (i+j > x):
                break
            store[i+j] = True
    
    s = 0
    max = 0
    for x in r:
        if (store[x] is False):
            max = x
            s += x
            
    return store,abundants, max, s

def p23count(a,b):
    if (b is True):
        return a+b
    else:
        return a
    
def proper_divisors(x):
    return filter(lambda y: (y!=x), divisors(x))

def p23abundant(x):
    if (sum(proper_divisors(x)) > x):
        return True
    else:
        return False
    
def p24(x=10, max=1000000):
    array = [0]*x
    bools = [False]*x
    s =p24help(array, 0, bools,max,0)
    
    return s
    

def p24help(array, index, bools, max, number):
    l = len(array)
    if (index == l):
        #print array
        return array, number+1
    for i in range(l):
        if (bools[i] == False):
            array[index] = i
            bools[i] = True
            array, number = p24help(array, index+1, bools,max,number)
            bools[i] = False
            
            if (number==max):
                break
                
    return array,number
 
def p25(x=1000):
    j = 4
    f= p25fib(4)
    
    while (1):
        j*=2
        for i in p25fib(j, f[-2], f[-1]):
            if (len(str(i[0])) >= x):
                return i
            
def p25fib(x, a0=(0,0), a1=(1,1)):
    
    if (x==1):
        return [(1,1)]
        
    l = [a0, a1]
    for i in range(a1[1]+1, x):
        n = l[-2][0] + l[-1][0]
        l.append((n, i))
    return l[2:]
    
def longdiv(x, y, point=50):
    y = map(lambda c: int(c), str(y))
    y.extend([0]*(point - len(y)))
    answer = []
    i = 0
    while (i < point):
        n = y[i]
        answer.append(int(n/x))
        if (i < point-1):
            y[i+1] = 10*(n%x) + y[i+1]
        i+=1
    return reduce(lambda s, x: s + str(x), answer, "")
    
def p26(x=1000):
    d = 1
    for n in range(1, x):
        a = longdiv26(n, 1)[1]
        if (len(a) > d):
            d = n
    return d, longdiv26(d,1)
    
def longdiv26(x, y, point=5000):
    y = map(lambda c: int(c), str(y))
    y.extend([0]*(point - len(y)))
    remainders = []
    answer = []
    recur = -1
    i = 0
    while (i < point):
        n = y[i]
        answer.append(int(n/x))
        if (i < point-1):
            y[i+1] = 10*(n%x) + y[i+1]
            if (y[i+1] in remainders):
                recur =  remainders.index(y[i+1])
                i+=1
                break
            remainders.append(y[i+1])
        i+=1
    
    recursion = reduce(lambda s, x: s + str(x), answer[recur+1:], "")
    answer.insert(recur+1, '(')
    answer.insert(i+1, ')')
    answer.insert(1, '.')

    return reduce(lambda s, x: s + str(x), answer, ""), recursion
    
def p27(a=1000, b=1000):
    s = prime27(100000)
    brange = range(b+1)
    brange = filter(lambda x: s.is_prime(x) , range(-b,b+1))
    maxn = (0, -a,-b)
    for bi in brange:
        for ai in range(-bi-1, a):
            n = 0
            while (s.is_prime(p27func(ai,bi,n))):
                n+=1
            maxn = max((n, ai, bi), maxn)
            #print n,ai,bi
            
    return maxn
    

def p27func(a,b,n):
    return n**2 + a*n + b

class prime27():
    """answer: (71, -61, 971)"""
    def __init__(self, x=8):
        self.primes = primes(x)
        self.length = len(self.primes)
        
    def is_prime(self,a):
        if (self.primes[-1] < a):
            self.get_primes(a)
            return self.is_prime(a)
        elif (self.bsearch(self.primes,a)):
            return True
        else: return False
        
    def get_primes(self, a):
        while (self.primes[-1] < a):
            a = 2*a
            self.primes = primes(a)
            self.length = len(self.primes)
    
    def bsearch(self, lst, i):
        last = self.length-1
        first = 0
        
        while (last >= first):
            mid = (last+first)/2
            val = lst[mid]
            if (val > i):
                last = mid - 1
            elif (val < i):
                first = mid+1
            else:
                return True
            
        return False
        
        
def p28(x=1001):
    n = 1
    s = 1
    p = 1
    while (n <= x-2):
        for i in range(4):
            p += n + 1
            s+= p
        n += 2
    return s
    #return 4*(x/2+ 2*x -2 + topright28(x-2,2)) #- 3*((x/2)+ 1)
    
def topright28(x, i):
    if (x%2 == 0):
        raise Exception("Number must be odd")
    if ((x == -1) or (x == 1)):
        return i
    return i*(4*(x-2) + 4) + topright28(x-2, i+1)
    
def p29(x=100):
    r = range(2,x+1)
    pairs = p29pairs(r,r)
    pairs = map(p29baseform, pairs)
    pairs.sort()
    last = pairs[-1]
    for i in range(len(pairs) -2, -1, -1):
        if (last == pairs[i]):
            del pairs[i]
        else:
            last = pairs[i]
        
    #pairs = list(set(pairs))
    return len(pairs)
def p29baseform(x):
    x1 = x[0]
    x2 = x[1]
    n = 2
    lst = []
    while (n <= x1):
        c = 0
        while (x1%n == 0):
            c += 1
            x1 /= n
        if (c > 0):
            lst.append((n, c))
        n += 1
    
    lst = map(lambda n: (n[0], x2*n[1]), lst)
    
    return lst

def p29pairs(a,b):
    l = []
    for i in a:
        for j in b:
            l.append((i,j))
            
    return l

def p30():
    """ Only 6 figure numbers are possible"""
    dict = map(lambda x: x**5, range(10))
    lst = []
    for n in range (10, 10**6):
        nums = map(lambda x: int(x), str(n))
        s = 0
       # print nums
        for d in nums:
            s += dict[d]
        if (s == n):
            lst.append(n)
    return lst
    
#def p31(x=200):
#    coins = [1, 2, 5, 10,20,50,100,200]
#    database = [0]*x
#    for i in coins:
#        database[i-1] = 1
#    for n in range(1,x):
#        for i in coins:
#            if (n-i < 0):
#                break
#            database[n] += database[n - i]
#            
#    return database

def p31(x=200):
    coins = [1, 2, 5, 10,20,50,100,200]
    coins.reverse()
    database = np.zeros((len(coins), x + 1))
    database[0][200] = 1
    database[0][0] = 1
    i = len(coins) -1
    for i, c in enumerate(coins):
        if (i == 0):
            continue
        for j in range(x+1):
            prevcombos = database[i-1][j]
            if (prevcombos == 0):
                continue
            for k in range(j, x+1, c):
                database[i][k] += prevcombos

            
    return database

class p31coins():
    
    def __init__(coins, x):
        self.coins = coins
        self.x = x
        self.store = np.zeros(len(coins), x)
    
    def get_num_change(coin, leftover):
        d