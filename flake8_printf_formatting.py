import ast
from typing import Any, Generator, List, Tuple, Type

import importlib_metadata

MOD001 = "MOD001 do not use printf-style string formatting"


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.expressions: List[Tuple[int, int]] = []

    def visit_BinOp(self, node: ast.BinOp) -> None:
        if isinstance(node.op, ast.Mod) and isinstance(node.left, (ast.Str, ast.Bytes)):
            self.expressions.append((node.lineno, node.col_offset))
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col in visitor.expressions:
            yield line, col, MOD001, type(self)
