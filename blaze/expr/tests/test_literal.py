import pytest

from itertools import product
import operator

from blaze import literal, symbol, discover


def test_construction():
    assert literal(1).value == 1


def test_repr():
    assert repr(literal(2)) == 'literal(2)'
    assert repr(literal('a')) == "literal('a')"


@pytest.mark.parametrize(
    ['opname', 'lhs', 'rhs'],
    product(
        ['eq', 'ne', 'lt', 'gt', 'le', 'ge'],
        [1.0, 2.0, 3, -0.5] + list(map(literal, [1.0, 2.0, 3, -2])),
        [1, 2, 3.0, -0.5] + list(map(literal, [1, 2, 3, -2])),
    )
)
def test_literal_literal_ops(opname, lhs, rhs):
    x, y = literal(lhs), literal(rhs)
    op = getattr(operator, opname)
    assert op(x, y) == literal(
        op(getattr(lhs, 'value', lhs), getattr(rhs, 'value', rhs))
    )


@pytest.mark.parametrize(
    ['opname', 'lhs', 'rhs'],
    product(
        ['add', 'mul', 'sub', 'truediv', 'floordiv', 'pow'],
        [1.0, 2.0, 3] + list(map(literal, [1.0, 2.0, 3])),
        [1, 2, 3.0] + list(map(literal, [1, 2, 3])),
    )
)
def test_arith(opname, lhs, rhs):
    x, y = lhs, rhs
    op = getattr(operator, opname)
    assert op(x, y) == literal(
        op(getattr(lhs, 'value', lhs), getattr(rhs, 'value', rhs))
    )


@pytest.mark.parametrize(
    ['value', 'opname'],
    product(
        [1.0, 2, -3, -4.2],
        [
            'add', 'mul', 'sub', 'truediv', 'floordiv', 'pow',
            'eq', 'ne', 'lt', 'gt', 'le', 'ge'
        ]
    )
)
def test_arith_with_symbol(value, opname):
    s = symbol('s', discover(value))
    op = getattr(operator, opname)
    assert op(s, literal(value)).isidentical(op(s, value))
    assert op(literal(value), s).isidentical(op(value, s))
