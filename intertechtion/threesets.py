import unittest
#def threebits(array):
#    
#    # Get counts:
#    length = negs = zeros = posis = 0
#    for a in array:
#        length += 1
#        if a < 0:
#            negs += 1
#        elif a > 0:
#            posis += 1
#        else:
#            zeros += 1
#
#    i = j = 0
#    while ():
#
#    for i, a in enumerate(array[:]):


def dutchFlagSort(arr):
    n_index = 0
    p_index = len(arr) - 1

    i = 0
    while (i <=  p_index):
        if(arr[i] < 0):
            swap(arr, i, n_index)
            n_index += 1
            i += 1
        elif(arr[i] > 0):
            swap(arr, i, p_index)
            p_index -= 1
        else:
            i += 1
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


class Test(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(dutchFlagSort([-1, 2, 0,4, 9]), [-1, 0, 4, 9, 2])

if __name__ == '__main__':
    import sys 
    if len(sys.argv) >= 2 and sys.argv[1] == '--test':
        del sys.argv[1]
        print 'ljklj'
        unittest.main()
