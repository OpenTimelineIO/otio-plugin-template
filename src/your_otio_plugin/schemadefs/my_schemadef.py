"""
Simple schema for my thing
"""

import opentimelineio as otio


@otio.core.register_type
class MyThing(otio.core.SerializableObject):
    """A schema for my thing."""

    _serializable_label = "MyThing.1"
    _name = "MyThing"

    def __init__(
            self,
            arg1=None,
            argN=None
    ):
        otio.core.SerializableObject.__init__(self)
        self.arg1 = arg1
        self.argN = argN

    arg1 = otio.core.serializable_field(
        "arg1",
        doc="arg1's doc string"
    )

    argN = otio.core.serializable_field(
        "argN",
        doc="argN's doc string"
    )

    def __str__(self):
        return "MyThing({}, {})".format(
            repr(self.arg1),
            repr(self.argN)
        )

    def __repr__(self):
        return "otio.schema.MyThing(arg1={}, argN={})".format(
            repr(self.arg1),
            repr(self.argN)
        )
