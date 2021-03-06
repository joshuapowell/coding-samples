#!/usr/bin/env python


class LogicGate:
    """Logic Gate.

    Create logic gates with this easy abstraction.

    Example:

        >>> _gate = LogicGate("verify")
        >>> _gate.getLabel()
        verify
        >>> _gate.getOutput()
        None
        >>>

    """

    def __init__(self, label):
        """LogicGate Constructor.

        Define a logic gate by adding a label and evaluating output.

        :param (object) self
            An object representing LogicGate.
        :param string label
            A generic string that represents the LogicGate

        :note
            output is not collected from the constructor, because output
            needs to be "performed" not defined.
        """
        self.label = label
        self.output = None

    def getLabel(self):
        """Return the label of the current LogicGate.

        :param (object) self
            An object representing LogicGate.

        :return (string)
            The label set at time of construction/instantiation
        """
        return self.label

    def getOutput(self):
        """Return the output of the current LogicGate.

        :param (object) self
            An object representing LogicGate.

        :return (unknown)
            Return of performed logic gate.
        """
        self.output = self.perform()

        return self.output


"""Example Usage."""
_gate = LogicGate("verify")

print "%s" % _gate.getLabel()
