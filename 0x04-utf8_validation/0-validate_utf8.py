#!/usr/bin/env python3
"""
UTF8 Validation
===============

For us to determine if the given data set represents a valid UTF8
encoding, we will need to follow the rules of UTF8 encoding.

1. Identify the leading byte,
    *   For a 1-byte char, the byte starts with `0`.
    **  For a 2-byte char, the byte starts with `110`.
    *** For a 3-byte char, the byte starts with `1110`.
    ****For a 4-byte char, the byte starts with `11110`.

2. Then subsequent bytes,
    * All subsequent bytes in a multi-byte char starts with `10`.

3. Follow validation steps.
    *   Iterate through the list of given integers.
    **  Determine the number of bytes for each char based on the leading
        byte.
    *** Ensure that the subsequent bytes start with `10`.
    ****If any byte sequence does not conform to UTF-8 rules, return False
"""
from typing import List


def validUTF8(data: List) -> bool:
    """
    A function that validates a given data set as a representation of a
    valid UTF-8 encoding

    Args:
        data (List): List of data set.
    Returns:
        boolean: True of False based on validation results.
    """
    # initialise bytes count in the current UTF-8 char
    bytes = 0

    # masks to check the most significant bits
    # mask 1 is used to check if the most significant bit is 1
    # mask 2 is used to check if the second most significant bit is 0
    bit_mask1 = 1 << 7  # 10000000
    bit_mask2 = 1 << 6  # 01000000

    # enter a loop to iterate over each byte in the input data
    for byte in data:
        bit_mask = 1 << 7

        # process the bytes
        if bytes == 0:
            # determine / count the number of leading 1's
            # enter a while loop to check if the MSB of `byte` is 1
            # by comparing it with the bit_mask
            while bit_mask & byte:
                # if MSB of `byte` is one, increment bytes_count
                bytes += 1
                # right-shift bit_mask by one position
                bit_mask = bit_mask >> 1

            # consider 1-byte chars
            if bytes == 0:
                continue

            # for instances where bytes_count is less than 2 or greater
            # than 4, return False.
            if bytes == 1 or bytes > 4:
                return False
    return bytes == 0
