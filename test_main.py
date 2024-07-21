import Utils
import Locations
import pytest


def test_browser_names():
    browsers = ["chrome", "chromium", "brave", "edge"]

    for k in Locations.LOCATIONS.keys():
        assert k in browsers


def test_padding():
    lista = ['a', 'b', 'c']
    assert Utils.add_spaces(lista) == ['a     ', 'b     ', 'c     ']
