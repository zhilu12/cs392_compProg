#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    int bestCount;
    string bestWord;

    TrieNode() {
        for (int i = 0; i < 26; ++i) children[i] = nullptr;
        bestCount = 0;
        bestWord = "";
    }
};

TrieNode* getNode() {
    return new TrieNode();
}

void insert(TrieNode* root, const string& key, int count) {
    TrieNode* pCrawl = root;
    for (char ch : key) {
        int index = ch - 'a';
        if (!pCrawl->children[index]) {
            pCrawl->children[index] = getNode();
        }
        pCrawl = pCrawl->children[index];

        // Update best word/count at this node
        if (count > pCrawl->bestCount ||
            (count == pCrawl->bestCount && !pCrawl->bestWord.empty() && key < pCrawl->bestWord)) {
            pCrawl->bestWord = key;
            pCrawl->bestCount = count;
        } else if (count > pCrawl->bestCount && pCrawl->bestWord.empty()) {
            // If bestWord is empty and this is the first word
            pCrawl->bestWord = key;
            pCrawl->bestCount = count;
        }
    }
}

pair<string, int> searchPref(TrieNode* root, const string& key) {
    TrieNode* pCrawl = root;
    for (char ch : key) {
        int index = ch - 'a';
        if (!pCrawl->children[index]) {
            return {"", -1};
        }
        pCrawl = pCrawl->children[index];
    }
    if (pCrawl->bestCount == 0) return {"", -1};
    return {pCrawl->bestWord, pCrawl->bestCount};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    TrieNode* root = getNode();
    unordered_map<string, int> words;

    // process freq dict
    for (int i = 0; i < n; ++i) {
        string word;
        cin >> word;
        ++words[word];
    }

    // add words from dict into trie with counts
    for (const auto& [word, count] : words) {
        insert(root, word, count);
    }

    int q;
    cin >> q;
    ostringstream out;

    // process queries
    for (int i = 0; i < q; ++i) {
        string key;
        cin >> key;
        auto [w, c] = searchPref(root, key);
        if (c == -1) {
            out << "-1\n";
        } else {
            out << w << " " << c << "\n";
        }
    }

    cout << out.str();
    return 0;
}
