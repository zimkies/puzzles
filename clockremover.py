'''
FIXME: still needs to be solved
Functionality for clockremover. Start with a clock of n numbers, and  number k. Go around the clock, removing the k'th element each time until you remain with only 1 element. Return the number that is remaining

'''
import sys 

def dumb_clock_remover(n,k):
    clock = range(n)
    i = 0
    while len(clock) > 1:
        i = ((i + k - 1) % len(clock))
        del clock[i]
    return clock[0] + 1

def clock_remover(n,k):
    return clock_remover_helper(n, k, 0, 0)

def clock_remover_helper(n,k, window, index):
    '''Cool Solutions - use a sliding window and compute the answer for 
    each window at a time

    n is the number of numbers on the clock
    k is the jump between numbers
    window is the index of which window we are calculating for
    index is the starting index on the clock
    
    '''
    interval = min(INTERVAL, n)
    clock = range(interval)
    other = n-interval
    remainder = k

    while len(clock) > 0:
        # Delete from our clock range
        j = remainder
        while j < len(clock)
            del clock[j]
            j += k - 1 
        other, remainder = my_cool_func(other, len(clock))
    
    # If we've deleted the clock, then it wasn't in that interval. Try it again with the next interval:
    newlength = n - my_cool_func(window*interval, 0, k)
    return clock_remover_helper(newlength, window+1)

def my_cool_func(length, start, jump):
    '''
    Takes a length of numbers, a starting index, a jump count,
    and returns (length, over) 
    length: the new length of numbers (after removing all hit numbers
    in the sequence starting at index i and jumping every j)
    over: The index we've arrived at past the end of the line
    '''
    hit = (length + jump -(start + 1) / jump
    over = start - length % jump 
    return (length - hit, over)

    
def main():
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print dumb_clock_remover(n,k)

if __name__ == '__main__':
    main()
