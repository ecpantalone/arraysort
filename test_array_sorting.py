from arrayClass import Sorter

sorter = Sorter() # new Sorter() object

# test to establish correct test syntax
def test_one():
    assert sorter.first_function(3) == 3

# tests sorting individual letters
def test_letters():
    assert sorter.sort(['c', 'b', 'a']) == ['a', 'b', 'c']