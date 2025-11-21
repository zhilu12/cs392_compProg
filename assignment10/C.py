class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.bestCount = 0
        self.bestWord = None

def getNode():
    pNode = TrieNode()
    pNode.isEndOfWord = False
    return pNode

def insert(root, key, count):
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if not pCrawl.children[index]:
            pCrawl.children[index] = getNode()
            
        pCrawl = pCrawl.children[index]

        if (count > pCrawl.bestCount or 
            (pCrawl.bestWord is None or key < pCrawl.bestWord)):
            pCrawl.bestWord = key
            pCrawl.bestCount = count
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
  
def searchPref(root, key):
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if not pCrawl.children[index]:
            return -1, _
        pCrawl = pCrawl.children[index]
    
    return pCrawl.bestWord, pCrawl.bestCount

from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    root = getNode()
    temp = []
    words = defaultdict(int)

    # process freq dict
    for _ in range(n):
        word = str(input())
        words[word] += 1

    # add words from dict into trie with counts
    for (word, count) in words.items():
        insert(root, word, count)

    # process queries
    q = int(input())

    for _ in range(q):
        key = str(input())
        temp.append(searchPref(root, key))
    for word, count in temp:
        if word == -1:
            print(-1)
        else:
            print(word, count)
    