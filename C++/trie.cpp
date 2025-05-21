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

    void insert(string word)
    {
    }

    void search(string word)
    {
    }
};