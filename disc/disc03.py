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
# my solution for sevens--function  
def has_seven(n):
    if(n == 0):
        return False
    elif(n % 7 == 0 or n % 10 == 7):
        return True
    else:
        return has_seven(n // 10)
    
def sevens(n,k):
    count = 0
    who = 1
    direction = 1
    start = 1
    curr = start
    while(True):
        if(has_seven(curr)):
            direction = - direction
        if(who > k):
                who = 1
        if(who < 1):
                who = k
        if(curr == n):
            return who
        who += direction
        curr += 1
        count += 1
        if(count == 60):
            return False

 # the standard solution
def sevens(n, k):
    """
    Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who += direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)
    
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
           

