"""Write a short Python function, is_even(k),
that takes an integer value and returns True if k is even,and False otherwise.
However, your function cannot use the multiplication, modulo, or division operators."""

def is_even(k):
    """Return true if found in for"""
    found = False
    for val in range(0, k+1, 2):
        if k == val:
            found = True
            break
    result = 'True' if found is True else 'False'
    print(result)
