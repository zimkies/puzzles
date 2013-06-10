'''
Takes 4 numbers and tries to find an algebraic combination of them that evaluates to 24
eg "1 2 3 4": 1*2*(3*4) = 24
Note this is not the most efficient solution but it works
'''
import sys

def check24(numbers):

    # error checking.. none for now

    # Set up data structures
    sequence = [None]*15
    ops = list("+1*/")
    numbers_mask = [0,0,0,0]

    # algorithm which sets up the permutation and calls a helper function which checks if its valid and 24
    # This will alternate over numbers first, then  operators, then brackets
    print permutations(sequence, ops, numbers, numbers_mask, 0)

    return

def permutations(sequence, ops, numbers, numbers_mask, level):
    if (level == 15):
        if (correct24(sequence)):
            return 1
        else:
            return 0

    elif (level in range(0, 15, 4)):
        count = 0
        sequence[level] = '('
        count += permutations(sequence, ops,  numbers,numbers_mask, level+1)
        sequence[level] = ' '
        count += permutations(sequence, ops, numbers,numbers_mask,level+1)
        return count



    elif (level in range(2, 15, 4)):
        count = 0
        sequence[level] = ')'
        count += permutations(sequence,ops,  numbers,numbers_mask, level+1)
        sequence[level] = ' '
        count += permutations(sequence,  ops, numbers,numbers_mask, level+1)
        return count

    elif (level in range(1, 15, 4)):
        count = 0
        for i in range(len(numbers)):
            if (numbers_mask[i] == 0):
                numbers_mask[i] = 1
                sequence[level] = numbers[i]
                count += permutations(sequence, ops,  numbers,numbers_mask, level+1)
                numbers_mask[i] = 0
        return count

    elif (level in range(3, 15, 4)):
        count = 0
        for i in range(len(ops)):
            sequence[level] = ops[i]
            count += permutations(sequence, ops,  numbers,numbers_mask, level+1)
        return count

def correct24(sequence):
    string = reduce(lambda w, x: w + str(x), sequence)
    try:
        x = eval(string)
        if (x == 24):
            print string, x
        return 1
    except:
        return 0

if __name__ == "__main__":
    check24(sys.argv[1].split(' '))
