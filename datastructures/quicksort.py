def quicksort(list):
    
    # error checking?
    l = len(list)
    if l <= 1:
        return list
     
    # Call hquicksort:
    hquicksort(list, 0, l-1)
    return list
    
def hquicksort(list, start,fin):
    
    # error checking?
    l = fin-start
    if l <= 1:
        return
    
    # Choose pivot and move it to the right
    list[start+l/2], list[fin] = list[fin], list[start+l/2]
    pivot = list[fin]
    # Reorder left and rstartght
    i,j = start, fin-1
    while(i < j):
        if (list[i] > pivot):
            # Rewind end pointer to next 'small' number
            while((list[j] > pivot) and (i <j)):
                j -=1
            if (i>= j):
                break
            # then switch the small and the big number
            list[i],list[j] = list[j],list[i]
        i+=1
    
    # Swap pivot with the first 'bigger' element
    if (pivot > list[j]):
        j += 1
    list[fin], list[j] = list[j], list[fin]
    
    
    # Recurse. Note cases where boundaries are negative don't matter because of error checking.
    hquicksort(list, start, j-1)
    hquicksort(list, j+1, fin)