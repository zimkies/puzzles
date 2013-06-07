import unittest

def primeintesrange(a,b):
    '''Returns the number of ints between a and b  inclusive who have prime numbers of 1 bits'''
    return primeints(a+1) - primeints(b)

def primeints(a):
    '''Returns the number of ints < a who have prime numbers of 1 bits'''
    bit_length = bitlength(a)
    primelist = superprimes(bit_length)
    ints = 0
    for j in setbitpositions(a):
        primelist = filter(lambda x: x>=0 and x <= j-1, primelist)
        for p in primelist:
            ints += choose(j-1,p)
        primelist = map(lambda x: x-1, primelist)
    return ints

def choose(n, p):
    return (factorial(n))/(factorial(n-p)* factorial(p))

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def bitlength(a):
    '''Returns how many bits are needed to represent this int up to the greatest bit'''
    i = 0
    while a:
        i +=1
        a = a >> 1
    return i

def setbitpositions(a):
    '''Returns a list of positions where the 1 bit is set in theint a'''
    positions = []
    i = 1
    while a:
        if a & 1:
            positions.append(i)
        i += 1
        a = a >> 1
    return list(reversed(positions))

def primes(n):
    '''Returns a list of primes up to n'''
    if n <= 0:
        return []
    a = range(2,n+1)
    for x in a:
        comp=[]
        for y in range(a.index(x),len(a)):
            q = x*a[y]
            if q<=max(a):
                comp.append(q)
            else:
                break
        for z in comp:
            a.remove(z)
    return a

def superprimes(n):
    '''Returns a list of primes up to n'''
    if n >= 1:
        return [1]+ primes(n)
    else:
        return primes(n) 


def primeintscheat(a):
    '''How many ints <= 1 have prime bits'''
    total = 0
    while a:
        if isprimebitint(a):
            total += 1
        a -= 1
    return total
        
#    if not a:
#        return 0
#    if isprimebitint(a):
#        return 1 + primeintscheat(a-1)
#    else:
#        return primeintscheat(a-1)

def isprimebitint(a):
    '''Does a have prime bits?'''
    return len(setbitpositions(a)) in superprimes(bitlength(a))
    


class TestSequenceFunctions(unittest.TestCase):
    def test_all(self):
    
        # primeints
        self.assertEqual(setbitpositions(0), [])
        self.assertEqual(setbitpositions(1), [1])
        self.assertEqual(setbitpositions(4), [3])
        self.assertEqual(setbitpositions(5), [3,1])
        self.assertEqual(setbitpositions(7), [3,2,1])
    
        # primes
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(1), [])
        self.assertEqual(primes(2), [2])
        self.assertEqual(primes(10), [2, 3,5, 7])
    
        # primes and 1
        self.assertEqual(superprimes(0), [])
        self.assertEqual(superprimes(1), [1])
        self.assertEqual(superprimes(2), [1, 2])
        self.assertEqual(superprimes(3), [1, 2, 3])
        self.assertEqual(superprimes(10), [1, 2, 3,5, 7])
    
    
        # bit _length
        self.assertEqual(bitlength(0), 0)
        self.assertEqual(bitlength(1), 1)
        self.assertEqual(bitlength(5), 3)
    
        # factorial
        self.assertEqual(factorial(0), 1) 
        self.assertEqual(factorial(1), 1) 
        self.assertEqual(factorial(3), 6) 
    
        # choose
        self.assertEqual(choose(1,1), 1) 
        self.assertEqual(choose(4,1), 4) 
        self.assertEqual(choose(3,2), 3) 
    
        # isprimebitint
        self.assertEqual(isprimebitint(0), False)
        self.assertEqual(isprimebitint(1), True)
        self.assertEqual(isprimebitint(3), True)
        self.assertEqual(isprimebitint(15), False)
    
        self.assertEqual(primeintscheat(1), 1)
        self.assertEqual(primeintscheat(2), 2)
        self.assertEqual(primeintscheat(3), 3)
        self.assertEqual(primeintscheat(4), 4)
        self.assertEqual(primeintscheat(16), 15)
    
    
        # primeints
        self.assertEqual(primeints(2), primeintscheat(1))
        self.assertEqual(primeints(4), primeintscheat(3))
        self.assertEqual(primeints(5), primeintscheat(4))
        
        self.assertEqual(primeints(16), primeintscheat(15))
        self.assertEqual(primeints(100), primeintscheat(99))
        self.assertEqual(primeints(133), primeintscheat(132))
        self.assertEqual(primeints(889), primeintscheat(888))
        self.assertEqual(primeints(2354889), primeintscheat(2354888))


if __name__ == '__main__':
    unittest.main()
