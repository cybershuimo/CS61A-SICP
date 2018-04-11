def announce(previous_score):
    def say(score0, score1):
        change0 = score0 - previous_score
        change1 = score1 - previous_score

        if change0 > 0:
            print("score0 is bigger than previous_score.")
            return announce(score0)
        elif change1 > 0:
            print("score1 is bigger than previous_score.")
            return announce(score1)
        else:
            return announce(previous_score)
    return say

def announce_highest(who, previous_high=0, previous_score=0):
    '''
    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(11, 0)
    >>> f2 = f1(11, 1)
    1 point! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 1)
    >>> f4 = f3(5, 20) # Player 1 gets 4 points, then Swine Swap applies
    19 points! That's the biggest gain yet for Player 1
    >>> f5 = f4(20, 40) # Player 0 gets 35 points, then Swine Swap applies
    20 points! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 55) # Player 1 gets 15 points; not enough for a new high
    '''
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if not who:
            score = score0
        else:
            score = score1
        change = score - previous_score
        if change > previous_high:
            if change == 1:
                print(change,'point! That\'s the biggest gain yet for Player', who)
            else:
                print(change,'points! That\'s the biggest gain yet for Player', who)
            return announce_highest(who, change, score)
        else:
            return announce_highest(who, previous_high, score)
    return say
