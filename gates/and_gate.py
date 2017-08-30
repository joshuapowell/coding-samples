#!/usr/bin/env python


from binary_gate import BinaryGate


class AndGate(BinaryGate):
    """And Gate.

    Create "and" logic gates.


    Truth Table:

        and    0      1

         0  |  0   |  0  |

         1  |  0   |  1  |


    """

    def __init__(self, label):
        """BinaryGate Constructor.

        Define a binary logic gate by adding a label.

        :param (object) self
            An object representing BinaryGate
        :param (string) label
            A generic string that represents the LogicGate

        """
        BinaryGate.__init__(self, label)

    def perform(self):

        _returnValue = 0

        _pinA = _gate.getPinA()
        _pinB = _gate.getPinB()

        if _pinA == 1 and _pinB == 1:
            _returnValue = 1

        return _returnValue



"""Example Usage."""
_gate = AndGate("verify")

_results = _gate.perform()

print _results
