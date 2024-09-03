#!/usr/bin/python3
"""Prime Game Algorithm
"""


def SieveOfEratosthenes(nums):
    """ Sieve and return all prime numbers up to n (inclusive).
    """
    if not nums:
        return None

    n = max(nums)
    if n < 2:
        return None

    prime = [True] * (n + 1)

    #initialize first prime number
    p = 2

    while(p * p <= n):
        # if prime[p] is not changed, then it is a prime number
        if prime[p] == True:
            # update all multiples of p to be marked as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    """ isWinner algorithm that determines the winner of a prime number
    choosing game.
    """
    if x < 1 or not nums:
        return None


if __name__ == "__main__":
    print(SieveOfEratosthenes([2, 5, 1, 4, 3]))
