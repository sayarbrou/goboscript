from pathlib import Path

from gparser import gparser, literal
from lark.lexer import Token
from lark.tree import Tree
from lark.visitors import Transformer
from lib import EXT


class gIncluder(Transformer[Token, Tree[Token]]):
    def __init__(self, project: Path):
        super().__init__()
        self.project = project

    def declr_use(self, args: tuple[Token]) -> Tree[Token]:
        path = self.project / f"{literal(args[0])}.{EXT}"
        return gparser.parse(path.read_text())
