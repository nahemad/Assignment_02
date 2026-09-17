from main import *

# Feel free to expand and add your own tests here.
# Doing so won't impact the gradescope autograder tests (gradescope uses
# its own copy of this file so any changes you make here won't affect it).

# 5 pts
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

# 5 pts
def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2