# Here's how i implement the swipe function

# def split(n):
#     return n // 10, n % 10

# def order_print(n):
#     if (n < 10):
#         print(n)
#     else:
#         all_but_last,last = split(n)
#         print(last)
#         order_print(all_but_last)

# def r_order_print(n):
#     if(n < 10):
#         print(n)
#     else:
#         all_but_last,last = split(n)
#         r_order_print(all_but_last)
#         print(last)

# def swipe(n):
#     order_print(n)
#     count = 0
#     tmp = n
#     while(tmp > 10):
#         count += 1
#         tmp //= 10
#     r_order_print(n % 10**count)




# Here's how to implement swipe function according to the standard answer
def swipe(n):
    if(n < 10):
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

def skip_fac(n):
    if(n <= 2):
        return n
    else:
        return n * skip_fac(n - 2)

def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if(n == 1):
        return 1
    elif(n % 2 == 0):
        return 1 + hailstone(n // 2)
    elif(n % 2 != 0):
        return 1 + hailstone(3 * n + 1)

