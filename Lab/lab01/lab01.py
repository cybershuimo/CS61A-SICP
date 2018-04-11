"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    if n <= 0:
        pass
    else: # n should be positive integer
        value = f(x)
        n -= 1
        while n > 0:                
            value = f(value)
            n -= 1
        return value



def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    if n < 0:
        raise ValueError('Argument should be nonnegative integer.')
    else:
        sum_result = 0
        while n // 10:
            sum_result += n % 10
            n = n // 10
        sum_result += n % 10
        return sum_result
        

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    if n < 0:
        raise ValueError('Argument should be nonnegative integer.')
    else:
        adjacent_eight = False
        while n // 10:
            if n % 10 == 8 and (n // 10) % 10 == 8:
                adjacent_eight = True
                return adjacent_eight
            else:
                n = n // 10
        return adjacent_eight

if __name__ == "__main__":
    import doctest
    doctest.testmod()