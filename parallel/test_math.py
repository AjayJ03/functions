import pytest
from pytest import mark

@mark.smoke
def test_chum1():
    print("chum1")

@mark.smoke
def test_chum2():
    print("chum2")

@mark.regression
def test_chum3():
    print("hello")

