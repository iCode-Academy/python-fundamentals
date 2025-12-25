import sys
sys.path.insert(0, '..')
from main import greet


def test_greet_world():
    """Test greeting with 'World'"""
    assert greet("World") == "Hello, World!"


def test_greet_alice():
    """Test greeting with 'Alice'"""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty():
    """Test greeting with empty string"""
    assert greet("") == "Hello, !"
