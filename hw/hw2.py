# Name: Gaurav Garg
# Email: garggaurav@berkeley.edu

from operator import mul, add

def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    i = 1
    prod = 1
    while i<=n:
        prod = prod * term(i)
        i = i+1
    return prod



def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    return product(n, int)

# Q2.

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    i = 1
    res = start
    while i <= n:
        res = combiner(res, term(i))
        i = i+1
    return res
    


def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    return accumulate(mul, 1, n, term)

# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    return lambda x: f(f(x))


# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    i = 1
    temp = f
    while(i<n):
        temp = compose1(temp, f)
        i=i+1

    return temp
    
    
def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h
