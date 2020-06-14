def selection_sort(lst):
    '''
    >>> lst = [54,26,93,17,77,31,44,55,20]
    >>> selection_sort(lst)
    >>> lst
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    for i in range(len(lst) -1, 0, -1):
        idx_max = 0
        for j in range(1, i+1):
            if lst[j] > lst[idx_max]:
                idx_max = j
        lst[i], lst[idx_max]= lst[idx_max], lst[i]

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')

'''
runtime is O(n^2)
5 7 2 9 1 / 0 idx_max
  j     i
5 7 2 9 1 / 1 idx for 7
    j   i
5 7 2 9 1 / 1 idx for 7
      j i
5 7 2 9 1 / 3 idx for 9
        ji
5 7 2 1 9

5 7 2 1   / 0
  j   i
5 7 2 1   / 1 idx for 7
    j i
5 7 2 1   / 1
      ji
5 1 2 7 9

5 1 2     / 0
  j i
5 1 2     / 0 idx for 5
    ji
2 1 5 7 9

2 1       / 0
  ji
1 2 5 7 9

'''