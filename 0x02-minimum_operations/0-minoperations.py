#!/usr/bin/python3
"""
There is a single character H in a text file.
Only two operations can be executed by the text editor:
    Copy All
    Paste

Given a number (n), a method should be generated that calculates
the fewest number of operations needed to result in exactly n of H
characters in the file.

Approaching this task using Prime Factorization.
The problem can be reduced to finding the sum of the prime factors of
the target number n.
"""
from typing import List


def prime_factors(n: int) -> List[int]:
    """
    Generates the prime factors of a given number n.

    Args:
        n (int): Target number to generate prime factors of.

    Returns:
        List[int]: A list of all prime factors of the target number
    """
    # if n is impossible to achieve.
    # if n cannot return a prime factor because it is 1 or less than 1
    # return 0
    if n <= 1:
        return [0]

    factors = []

    # divide n by 2 until n is odd
    while n % 2 == 0:
        # while n divided by 2 returns no reminder, append list with first
        # prime factor 2
        factors.append(2)
        # divide n by 2 - breaking down even numbers till while condition
        # can no longer be met
        n //= 2

    # divide n by odd numbers from 3 up to sqrt(n)
    # move to next least prime factor 3
    factor = 3
    while factor * factor <= n:  # while square of factor is <= n
        while n % factor == 0:
            # while n divided by factor returns no reminder, append list
            # with factor
            factors.append(factor)
            n //= factor
        factor += 2  # move to the next odd number

    # if n is still greater than 2, then it is prime
    if n > 2:
        factors.append(n)

    return factors


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in
    n of H characters in a given file

    Args:
        n (int): Target number of characters to achieve

    Returns:
        Int: Fewest number of operations generated to match n chars
    """
    return sum(prime_factors(n))

# print(prime_factors(12))
# print(minOperations(12))
