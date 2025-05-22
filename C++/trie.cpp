#include <map>
#include <string>

using namespace std;

class TrieNode
{
public:
    bool isLeaf = false;
    map<char, TrieNode *> children;
};

class Trie
{
public:
    TrieNode *root;
    Trie()
    {
        root = new TrieNode();
    }

    /**
     * Insert a word into the trie
     */
    void insert(string word)
    {
        TrieNode *cur = root;
        for (char c : word)
        {
            // Character not found
            if (cur->children.find(c) == cur->children.end())
            {
                cur->children[c] = new TrieNode();
            }
            cur = cur->children[c];
        }
        cur->isLeaf = true;
    }

    /**
     * Search if the word is in the trie
     */
    bool search(string word)
    {
        TrieNode *cur = root;
        for (char c : word)
        {
            // Word not in trie
            if (cur->children.find(c) == cur->children.end())
            {
                return false;
            }
            cur = cur->children[c];
        }
        return cur->isLeaf;
    }

    /**
     * Search if the given string is a prefix in the trie
     */
    bool isPrefix(string prefix)
    {
        TrieNode *cur = root;
        for (char c : prefix)
        {
            // Prefix not in trie
            if (cur->children.find(c) == cur->children.end())
            {
                return false;
            }
            cur = cur->children[c];
        }
        return true;
    }
};