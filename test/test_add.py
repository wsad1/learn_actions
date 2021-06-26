from src.add import add_ints
import pytest

def test_add():
	assert add_ints(5,6) == 11
