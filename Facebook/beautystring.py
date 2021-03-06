'''
When John was a little kid he didn't have much to do. There was no internet, no Facebook, 
and no programs to hack on. So he did the only thing he could... he evaluated the beauty 
of strings in a quest to discover the most beautiful string in the world.
 
Given a string s, little Johnny defined the beauty of the string as the sum of the beauty
of the letters in it.
 
The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have
the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so
that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as 
lowercase 'f', for example.)
 
You're a student writing a report on the youth of this famous hacker. You found the string 
that Johnny considered most beautiful. What is the maximum possible beauty of this string?
 
Input
The input file consists of a single integer m followed by m lines.
Output
Your output should consist of, for each test case, a line containing the string "Case #x: y" 
where x is the case number (with 1 being the first case in the input file, 2 being the 
second, etc.) and y is the maximum beauty for that test case.
 
Constraints
5 ≤ m ≤ 50
2 ≤ length of s ≤ 500
 
 
Example input                                                       Example output
5
ABbCcc                                                          Case #1: 152
Good luck in the Facebook Hacker Cup this year!                     Case #2: 754
Ignore punctuation, please :)                                       Case #3: 491
Sometimes test cases are hard to make up.                           Case #4: 729
So I just go consult Professor Dalves                               Case #5: 646
'''
import sys
import operator

def max_beauty(string):
    beauty = 0

    # Dictionarize it
    counts = {}
    for l in string:
        if l.isalpha():
            counts[l.lower()]  = counts.get(l.lower(), 0) + 1
        
    # Create sorted list
    sortedcounts = sorted(counts.itervalues(), reverse=True)

    # Iterate through list and add value
    currentval = 26
    for i in sortedcounts:
        beauty += currentval*i
        currentval -= 1

    return beauty

       

    return 5

if __name__ ==  '__main__':
    filep = open(sys.argv[1])
    m  = int(filep.readline())
    for i, line in enumerate(filep):
        string = line
        beauty = max_beauty(string)
        print 'Case #%d: %d' % (i+1, beauty)
