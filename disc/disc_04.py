def paths_solution1(m,n):
    count = 0
    def paths_add(x,y):
        nonlocal count
        if(x == m and y == n):
            count += 1
            return
        if(x < m):
            paths_add(x + 1,y)
        if(y < n):
            paths_add(x, y + 1)
    paths_add(1,1)
    return count

def paths_solution2(m,n):
    if(m == 1 or n == 1):
        return 1
    else:
        return paths_solution2(m - 1,n) + paths_solution2(m,n - 1)

def max_product(s):
    if(len(s) == 1):
        return s[0]
    if(s == []):
        return 1
    else:
        return max(s[0] * max_product(s[2:]),max_product(s[1:]))
    
def sums(n,m):
    if(n < 0):
        return [] # No list can satisfy the question 
    if(n == 0):
        return [[]] # the only way to satisfy the question is [] with all numbers positive
    result = []
    for k in range(1,m + 1):
        result += [[k] + rest for rest in sums(n - k,m) if(rest == [] or rest[0] != k)]
    return result