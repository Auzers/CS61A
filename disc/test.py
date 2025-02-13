class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def range_Link(start, end):
    """
    >>> range_Link(3,6)
    Link(3, Link(4, Link(5)))
    """
    # end -= 1
    # res = Link.empty
    # while(end >= start):
    #     res = Link(end, res)
    #     end -= 1
    # return res
    if(start >= end):
        return Link.empty
    else:
        return Link(start,range_Link(start + 1, end))

def map_Link(f, s):
    if(s == Link.empty):
        return s
    else:
        return Link(f(s.first), map_Link(s.rest))

def filter_Link(f, s):
    if(s == Link.empty):
        return s
    elif(f(s)):
        return Link(s.first, filter_Link(f, s.rest))
    elif(not f(s)):
        return Link(filter_Link(f,s.rest))
    

        