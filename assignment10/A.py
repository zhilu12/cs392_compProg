class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.numChildren = [0] * 26

def getNode():
    pNode = TrieNode()
    pNode.isEndOfWord = False
    return pNode

def insert(root, key):
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        pCrawl.numChildren[index] += 1
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


def searchLCP(root, key):
    lps = 0
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if pCrawl.numChildren[index] > 1:
          lps += 1
        if not pCrawl.children[index]:
            return False
        pCrawl = pCrawl.children[index]
        
    return lps


if __name__ == '__main__':
    keys = []
    N = int(input())
    for _ in range(N):
      keys.append(str(input()))
      
    root = getNode()
    for i in range(len(keys)):
        insert(root, keys[i])
    
    for key in keys:
      print(searchLCP(root, key))