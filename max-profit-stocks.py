def max_profit(prices):
    """
    >>> max_profit([7,1,5,3,6,4])
    7
    >>> max_profit([1,2,3,4,5])
    4
    """
    profit = 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx-1]:
            profit += prices[idx] - prices[idx-1]

    return profit

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed.")