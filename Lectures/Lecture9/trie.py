class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

def getNode():
    pNode = TrieNode()
    pNode.isEndOfWord = False
    return pNode

def insert(root, key):
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if not pCrawl.children[index]:
            pCrawl.children[index] = getNode()
        pCrawl = pCrawl.children[index]
    pCrawl.isEndOfWord = True

def search(root, key):
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if not pCrawl.children[index]:
            return False
        pCrawl = pCrawl.children[index]
    return pCrawl and pCrawl.isEndOfWord

def isEmpty(root):
    for i in range(26):
        if root.children[i]:
            return False
    return True

def remove(root, key, depth = 0):
    if not root:
        return None

    if depth == len(key):
        if root.isEndOfWord:
            root.isEndOfWord = False
        if isEmpty(root):
            del root
            root = None
        return root

    index = ord(key[depth]) - ord('a')
    root.children[index] = remove(root.children[index], key, depth + 1)

    if isEmpty(root) and not root.isEndOfWord:
        del root
        root = None
    return root

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "hero", "heroplane"]
    root = getNode()
    for i in range(len(keys)):
        insert(root, keys[i])
    if search(root, "the"):
        print("Yes")
    else:
        print("No")
    if search(root, "these"):
        print("Yes")
    else:
        print("No")
    root = remove(root, "heroplane")
    if search(root, "hero"):
        print("Yes")
    else:
        print("No")