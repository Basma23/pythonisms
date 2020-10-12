from pythonisms import __version__
from pythonisms.pythonisms import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_equality():
    ll = LinkedList(['B', 'a', 's', 'm', 'a'])
    ll1 = LinkedList(['B', 'a', 's', 'e', 'm', 'a', 'h'])
    assert (ll == ll1) == False

def test_str():
    ll = LinkedList(['B', 'a', 's', 'm', 'a'])
    actual = ll.__str__()
    expected ='[B] -> [a] -> [s] -> [m] -> [a] -> None'
    assert actual == expected

def test_get_item():

    ll = LinkedList(['B', 'a', 's', 'm', 'a'])
    assert ll[0] == 'B'
    assert ll[1] == 'a'
    assert ll[2] == 's'
    assert ll[3] == 'm'
    assert ll[4] == 'a'


