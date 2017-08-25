#!/usr/bin/env python

"""Algorithms Section, An example of a top-down approach.

Builds call stack of size O(n) making our total memory cost O(n). Meaning, that
as we continue to recurse or reverse engineer the problem the space it takes
continues to grow larger then once we multiple that by memory we can cause a
stack overflow error.

The problem below assumes that value `n` is greater than or equal to 1.

Also see "Longest common problem/subsequences"

"""


def product_1_to_n_oneline(n):
    """One-line solution."""

    return n * product_1_to_n_oneline(n-1) if n > 1 else 1

def product_1_to_n_multiline(n):
    """Multi-line solution."""

    """Step 1: Check to see if the `n` argument is greater than 1."""
    if n > 1:

        """Reduce `n` value by 1."""
        n_less_1 = n-1

        """Recur this method with the value produced by line 29."""
        value = product_1_to_n_multiline(n_less_1)

        return n * value

    """If `n` argument is ~not~ greater than 1, then return 1."""
    return 1
