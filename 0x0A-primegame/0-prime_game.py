#!/usr/bin/python3
"""Prime Game Algorithm
"""
# has a bug for working with a 10000 case.


def SieveOfEratosthenes(num):
    """ Sieve and return all prime numbers up to n (inclusive).
    """

    prime = [True] * (num + 1)

    # initialize first prime number
    p = 2

    while(p * p <= num):
        # if prime[p] is not changed, then it is a prime number
        if prime[p] is True:
            # update all multiples of p to be marked as non-prime
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    """ isWinner algorithm that determines the winner of a prime number
    choosing game.
    """
    if x < 1 or not nums:
        return None

    primes = SieveOfEratosthenes(max(nums))

    # hold wins made by each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_range = []
        for p in primes:
            if p <= n:
                primes_in_range.append(p)

        # maria should make the first move
        marias_turn = True

        while primes_in_range:
            prime = primes_in_range.pop(0)

            new_primes_in_range = []
            for p in primes_in_range:
                if p % prime != 0:
                    new_primes_in_range.append(p)

            primes_in_range = new_primes_in_range

            marias_turn = not marias_turn

        if marias_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    if ben_wins > maria_wins:
        return 'Ben'
    return None


if __name__ == '__main__':
    print(SieveOfEratosthenes(10000))
