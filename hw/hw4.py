# Name: Gaurav Garg
# Email: garggaurav@berkeley.edu


def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q1.

def interval(a, b):
    return (a, b)
    
def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]
# Q2.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert y!=0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    l = min((lower_bound(x) - upper_bound(y)), (upper_bound(x) - lower_bound(y)))
    u = max((lower_bound(x) - upper_bound(y)), (upper_bound(x) - lower_bound(y)))
    return interval(l, u)

# Q4.

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    """
    low_x = lower_bound(x)
    up_x = upper_bound(x)
    low_y = lower_bound(y)
    up_y = upper_bound(y)

    if low_x>=0 and up_x>=0 and low_y>=0 and up_y>=0:
        return interval((low_x*low_y), (up_x*up_y))

    if low_x<=0 and up_x<=0 and low_y<=0 and up_y<=0:
        return interval((up_x*up_y), (low_x*low_y))

    if low_x>=0 and up_x>=0 and low_y<=0 and up_y>=0:
        return interval((up_x*low_y), (up_x*up_y))

    if low_x<=0 and up_x>=0 and low_y<=0 and up_y<=0:
        return interval((up_x*low_y), (low_x*low_y))

    if low_x<=0 and up_x<=0 and low_y>=0 and up_y>=0:
        return interval((low_x*up_y), (up_x*low_y))

    if low_x>=0 and up_x>=0 and low_y<=0 and up_y<=0:
        return interval((up_x*low_y), (low_x*up_y))

    if low_x<=0 and up_x>=0 and low_y>=0 and up_y>=0:
        return interval((low_x*up_y), (up_x*up_y))

    if low_x<=0 and up_x<=0 and low_y<=0 and up_y>=0:
        return interval((low_x*up_y), (low_x*low_y))

    if low_x<=0 and up_x>=0 and low_y<=0 and up_y>=0:
        return interval(min((low_x*up_y),(up_x*low_y)), max((low_x*low_y),(up_x*up_y)))

# Q5.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    return interval(c-((c*p)/100), c+((c*p)/100))

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    c = (upper_bound(x) - lower_bound(x))//2 + lower_bound(x)
    return ((upper_bound(x) - c)*100)/c

# Q6.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
#(1,4) == (7,10)

# Q7.

def multiple_references_explanation():
  return """The resultant interval from operating on multiple interval is usually wider than the operand intervals. So every time intervals are operated on, they lose precision.
  In case of par1, this happens thrice. For par2, this happens only once. (Note: operating by an interval of kind (x, x) does not affect the precision.) 
  Hence, par2 is more precise than par1"""

# Q8.

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    xmin = lower_bound(x)
    xmax = upper_bound(x)
    xtreme = -b/(2*a)

    interval1 = a*xmin*xmin + b*xmin + c
    interval2 = a*xmax*xmax + b*xmax + c
    interval3 = a*xtreme*xtreme + b*xtreme + c

    if xtreme>xmin and xtreme<xmax:
        return interval(min(interval1, interval2, interval3), max(interval1, interval2, interval3))

    else:
        return interval(min(interval1, interval2), max(interval1, interval2))

# Q9.

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    result = (0,0)
    for x in seq:
        if non_zero(x):
            result = add_interval(result,square_interval(x))

    return result


from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval, list(map(square_interval, list(filter(non_zero, seq)))))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval, [square_interval(x) for x in seq if non_zero(x)])


