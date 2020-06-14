def bubble_sort(lst):
    '''
    >>> lst = [10,2,3,4,1]
    >>> bubble_sort(lst)
    >>> lst
    [1, 2, 3, 4, 10]
    '''
    for i in range(len(lst) -1):
        # -i to skip the end indexes with largest element at each iteration
        for j in range(len(lst) -1 -i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')

'''
runtime is O(n^2)
10 2 3 4 1
^ *
2 10 3 4 1
  ^ *
2 3 10 4 1
    ^ *
2 3 4 10 1
      ^ *

2 3 4 1
^
2 3 4 1
  ^
2 3 4 1
    ^ *


2 3 1 
^
2 3 1
  ^
 
2 1
^

'''