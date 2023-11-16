from .. import base

def apply():
    base.BaseElement._repr_latex_ = (
        lambda self: self.__text__()
    )
