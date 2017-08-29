#!/usr/bin/env python


from logic_gate import LogicGate


class BinaryGate(LogicGate):
    """Binary Gate.

    Create "binary" logic gates.
    """

    def __init__(self, label):
        """BinaryGate Constructor.

        Define a binary logic gate by adding a label.

        :param (object) self
            An object representing BinaryGate
        :param (string) label
            A generic string that represents the LogicGate

        """
        super(LogicGate, self).__init__(label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate %s: " % (self.getLabel())))

    def getPinB(self):
        return int(input("Enter Pin B input for gate %s: " % (self.getLabel())))


"""Example Usage."""
_gate = BinaryGate("verify")

_pinA = _gate.getPinA()
_pinB = _gate.getPinB()
