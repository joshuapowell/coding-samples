#!/usr/bin/env python


from logic_gate import LogicGate


class UnaryGate(LogicGate):
    """Unary Gate.

    Create "unary" logic gates.
    """

    def __init__(self, label):
        """UnaryGate Constructor.

        Define a unary logic gate by adding a label.

        :param (object) self
            An object representing UnaryGate
        :param (string) label
            A generic string that represents the LogicGate

        """
        super(LogicGate, self).__init__(label)

        self.pinA = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate %s: " % (self.getLabel())))


"""Example Usage."""
_gate = UnaryGate("verify")

_pinA = _gate.getPinA()
