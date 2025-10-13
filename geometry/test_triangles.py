"""Test the triangles module.

Name: YOUR NAME
Date: THE DATE
"""

from pytest import approx, raises
from triangles import valid, area, classify


def test_valid():
    # NOTE: You should never type "== True".
    assert valid((3, 4, 5))
    # NOTE: You should never type "== False".
    assert not valid((3, 4, 10))


def test_area():
    # NOTE: Use approx() to avoid floating-point errors.
    assert area((3, 4, 5)) == approx(6.0)


def test_classify():
    # NOTE: Use raises() to check if errors are raised.
    with raises(ValueError):
        classify((3, 4, 10))
