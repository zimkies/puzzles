# A function that returns true if there is a solux= "bnn
def check24(numbers):
    
    # error checking.. none for now
    
    # Set up data structures
    sequence = [None]*15
    operators = list("+1*/")
    operators = [0,0,0]
    numbers_mask = [0,0,0,0]
    
    # algorithm which sets up the permutation and calls a helper function which checks if its valid and 24
    # This will alternate over numbers first, then  operators, then brackets
    permutations(string, ops, numbers, numbers_mask, 0)
    
    return






def permutations(sequence, ops, numbers, numbers_mask, level):
    if (level == 15):
        if (correct24(sequence)):
            return 1
        else:
            return 0
    
    elif (level in range(0, 15, 4)):
        sum = 0
        sequence[level] = '('
        sum += permutations[sequence,   numbers,numbers_mask, level+1]
        sequence[level] = ' '
        sum += permutations[sequence,  numbers,numbers_mask,level+1]
        return sum

        
    
    elif (level in range(2, 15, 4):
        sum = 0
        sequence[level] = ')'
        sum += permutations[sequence,  numbers,numbers_mask, level+1]
        sequence[level] = ' '
        sum += permutations[sequence,   numbers,numbers_mask, level+1]
        return sum
    
    elif (level in range(1, 15, 4):
        sum = 0
        for i in range(len(numbers)):
            if (numbers_mask[i] == 0):
                numbers_mask[i] = 1
                sequence[level] = numbers[i]            
                sum += permutations(sequence, ops,  numbers,numbers_mask, level+1)
                numbers_mask[i] = 0
         return sum
    
    elif (level in range(3, 15, 4):
        sum = 0
        for i in range(len(ops)):
            sequence[level] = ops[i]            
            sum += permutations(sequence, ops,  numbers,numbers_mask, level+1)
        return sum

def correct24(sequence):
    string = str(sequence)
    try: 
        x = eval(string)
        if (x == 24):
            print string, x
        return 1
    except:
        return 0
    

    


