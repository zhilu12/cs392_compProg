# This code has bugs

def build(a, tree, i, tl, tr):
    if tl == tr:
        tree[i] = a[tl]
    else:
        tm = (tl + tr) // 2
        build(a, tree, i*2, tl, tm)
        build(a, tree, i*2+1, tm+1, tr)
        tree[i] = tree[i*2] + tree[i*2+1]

def update(tree, i, tl, tr, pos, new_val):
    if tl == tr:
        tree[i] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(tree, i*2, tl, 
                   tm, pos, new_val)
        else:
            update(tree, i*2+1, 
                   tm+1, tr, pos, new_val)
        tree[i] = tree[i*2] + tree[i*2+1]

def query(tree, i, tl, tr, l, r):
    if l > r:
        return 0
    if l == tl and r == tr:
        return tree[i]
    tm = (tl + tr) // 2
    return (query(tree, i*2, tl, tm, l, min(r, tm))+ query(tree, i*2+1, tm+1, tr, max(l, tm+1), r))
