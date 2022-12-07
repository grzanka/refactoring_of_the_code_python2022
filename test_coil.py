import pytest
from main import setup_coil

def test_coil_setup():
    coil = setup_coil()
    assert coil.position[0] == 0
    assert coil.position[1] == 0
    assert coil.position[2] == 0

    assert len(coil.children) == 8