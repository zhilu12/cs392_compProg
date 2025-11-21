max_b = 26

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def getNode():
    pNode = TrieNode()
    pNode.isEndOfWord = False
    return pNode

def insert(root, x, delta):
    node = root
    node.count += delta
    for b in range(max_b, -1, -1):
        bit = (x >> b) & 1
        if node.children[bit] is None:
            node.children[bit] = TrieNode()
        node = node.children[bit]
        node.count += delta

def cal_xor(root, p, l):
    node = root
    res = 0
    for b in range(max_b, -1, -1):
        if node is None:
            break
    
        pb = (p >> b) & 1
        lb = (l >> b) & 1

        if lb == 1:
            child_same = node.children[pb]
            print(pb)
            if child_same is not None:
                res += child_same.count

            node = node.children[pb ^ 1]

        else:
            node = node.children[pb]

    return res

res = []
root = TrieNode()

n = int(input())

for _ in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
        p = q[1]
        insert(root, p, 1)

    elif q[0] == 2:
        p = q[1]
        insert(root, p, -1)

    elif q[0] == 3:
        p, l = q[1], q[2]
        ans = cal_xor(root, p, l)
        res.append(ans)

    else:
        print("invalid")

print("\n".join(str(out) for out in res))