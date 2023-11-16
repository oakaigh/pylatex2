from .. import base

def apply():
    base.BaseElement.__str__ = (
        lambda self: self.__text__()
    )

    # TODO __format__
