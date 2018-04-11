def is_prime(n):
    '''
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    '''
    assert n > 0, 'n should be a positive integer'
    if n == 1:
        return False
    # if n > 1
    k = 2
    while k < n / 2:
        if n % k == 0:
            return False
        else:
            k = k + 1
    return True

# import sys
# print("hello %s" % sys.argv[1])


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# #main()	# cannot used alone?

def announce_highest(who, previous_score=0):
    '''
    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(11, 0)
    Score change in the turn is 0 for Player 1
    >>> f2 = f1(11, 1)
    Score change in the turn is 1 for Player 1
    >>> f3 = f2(1,3)
    Score change in the turn is 2 for Player 1
    '''
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if not who:
            score = score0
        else:
            score = score1
        change = score - previous_score
        print('Score change in the turn is', change, 'for Player', who)
        return announce_highest(who, score)
    return say