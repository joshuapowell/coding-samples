#!/usr/bin/env python


"""Fraction."""

class Fraction:
    """Fraction.

    Create fractions with this easy abstraction.

    Example:

        Given a numerator (top number) of 3 and a denominator (bottom number)
        of 5, the decimal representation would be 0.6.

        To calculate the decimal number from fractional notation we divide the
        numerator by the denominator.

            3 / 5 = 0.6

            or

            ```
            _fraction = Fraction(3, 5)
            _decimal = (_fraction.num/_fraction.den)
            ```

    Notes:

        Python 2.7 returns values of division problems as integers. In order
        to return a decimal representation, you must use one of the following
        two methods:

        Method 1:

            ```
            from __future__ import division
            ```

            An in-depth description of the reason and abstraction behind
            changing the divion operator can be found in PEP238.

            @see https://www.python.org/dev/peps/pep-0238/

        Method 2:

            Represent either the numerator or denominator as a float as shown
            below in the examples.

            ```
            3/5.0
            ```

            or

            ```
            3/float(5.0)
            ```

            or

            ```
            float(3)/5

    """

    def __init__(self, numerator, denominator):
        """Fraction Construction

        :param (object) self
            An object referencing Fraction.
        :param (int) numerator
            Numerator (top number) input of Fraction.
        :param (int) denominator
            Denominator (bottom number) input of Fraction.
        """

        self.num = float(numerator)
        self.den = float(denominator)

    def __str__(self):
        return "%s/%s" % (self.num, self.den)


_fraction = Fraction(3, 5)

print "%s/%s or %s" % (_fraction.num,_fraction.den,(_fraction.num/_fraction.den))
