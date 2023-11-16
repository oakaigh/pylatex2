import tempfile

from ... import base


class Package(base.BasePackage):
    @property
    def name(self):
        return 'graphicx'

class Preamble(base.BasePreamble):
    @property
    def __children__(self):
        return [
            Package()
        ]

class BaseGraphics(base.BaseElement):
    # TODO pathlike!!!!
    @property
    def _path_(self) -> str:
        ...

    # TODO Nothing!!!
    @property
    def _options_(self) -> str:
        ...

    def __text__(self):
        # TODO !!!!!!!!!!!!!!
        return (
            r'\includegraphics'
            + (rf'[{base.text(self._options_)}]' 
                if not base.isnothing(self._options_) else '')
            + rf'{{{self._path_}}}'
        )

# TODO hook for pre/post file reading!!!! in latex
# TODO only create temp files pre file reading
class BaseInlineGraphics(BaseGraphics):
    def __init__(
        self,
        content: bytes = None,
        ext: str = None,
        options: str = None,
    ):
        # TODO
        self._file = tempfile.NamedTemporaryFile(suffix=ext, buffering=0)
        if content is not None:
            self._file.write(content)
            self._file.flush()

        self._options = options

    @property
    def _options_(self):
        return self._options

    @property
    def _path_(self):
        return self._file.name

    # TODO with g: print(g.render())

    # TODO necessary? __enter_render__ __exit_render__
    # TODO use python obj ctx mgmt!!!

# TODO fnamestr or path-like or binary file-like
class Graphics(BaseGraphics):
    # TODO pathlike
    def __init__(self, path: str):
        self._path = path

    @property
    def _path_(self):
        return str(self._path)

# TODO
class InlineGraphics(BaseInlineGraphics):
    pass
