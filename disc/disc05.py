def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be tree'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    if(not branches(tree)):
        return True
    else:
        return False

def is_tree(tree):
    if(type(tree) != list or len(tree) < 1):
        return False
    else:
        for branch in branches(tree):
            if(not is_tree(branch)):
                return False
    return True

def has_path(t, p):
    if(p[0] == label(t) and len(p) == 1):
        return True
    if(p[0] == label(t)):
        return any([has_path(b,p[1:]) for b in branches(t)]) # 只要有一个是True则 返回值就是True
    return False

def find_path(t,value):
    if(label(t) == value):
        return [label(t)]
    for b in branches(t):
        path = find_path(b,value)
        if(path):
            return [label(t)] + path
    return None



