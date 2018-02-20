"""Write a short Python function, is_multiple(n, m), that takes two integer values
and returns True if n is a multiple of m, # that is, n = m is for some integer i,
and False otherwise."""

def is_multiple(number, multiple):
    """return whether number is a multiple or not"""
    result = ('True' if number % multiple == 0 else 'False')
    print(result)


sample = "balloon"[5] #{}