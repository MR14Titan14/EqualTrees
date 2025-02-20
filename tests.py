import pytest
from equalize import make_equal
from main import read_from_file

@pytest.mark.parametrize("path, expected",[
    ("input.txt",4),
    ("input2.txt", 4),
    ("input3.txt", 4),
    ("input4.txt", 0),
    ("input5.txt", 12),
])
def test_equal(path, expected):
    n, tree1, tree2 = read_from_file(path)
    oper,_ = make_equal(n,tree1,tree2)
    assert oper == expected