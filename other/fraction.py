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

            >>> from __future__ import division

            An in-depth description of the reason and abstraction behind
            changing the divion operator can be found in PEP238.

            @see https://www.python.org/dev/peps/pep-0238/

        Method 2:

            Represent either the numerator or denominator as a float as shown
            below in the examples.

            >>> 3/5.0

            or

            >>> 3/float(5.0)

            or

            >>> float(3)/5

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
        """Override built-in __str__ implementation.

        Overrides default of printing instance address. Provides the end-user
        with a mock representation of the Fraction in fractional notation.

        :param (object) self
            An object referencing Fraction.

        :return (str)
            A visual representation of the numerator and denominator displayed
            in mock fractional notation.
        """

        return "%s/%s" % (int(self.num), int(self.den))

    def __add__(self, toBeAdded):
        """Override built-in __add__ implementation.

        Overrides default addition due to built-ins inablility to add these
        fractional notations.

        Mathematical notation:

            a   c     ad   cb     ad+cb
            - + -  =  -- + --  =  -----
            b   d     bd   bd      bd

            1   1     ad   cb     ad+cb
            - + -  =  -- + --  =  -----
            4   2     bd   bd      bd

        Example:

            >>> _f1 = Fraction(1, 4)
            >>> _f2 = Fraction(1, 2)
            >>> _f3 = _f1+_f2
            6/8
            >>>

        """

        _numerator = (self.num*toBeAdded.den)+(toBeAdded.num*self.den)
        _denominator = (self.den*toBeAdded.den)

        return Fraction(_numerator, _denominator)


"""Example usage of the Fraction class."""
_fraction = Fraction(3, 5)

print _fraction

"""Attempt addition of two fractions."""
_f1 = Fraction(1, 4)
_f2 = Fraction(1, 2)
_f3 = _f1+_f2

print _f3
