#include <vector>
#include <string>

using namespace std;

/**
 * Build the Longest Prefix Suffix array
 *
 */
vector<int> buildLPS(string pattern)
{
    vector<int> lps(pattern.size(), 0);
    int prev = 0;
    int i = 1;
    while (i < pattern.size())
    {
        if (pattern[i] == pattern[prev])
        {
            lps[i] = ++prev;
            ++i;
        }
        else
        {
            if (prev == 0)
            {
                lps[i] = 0;
                ++i;
            }
            else
            {
                prev = lps[prev - 1];
            }
        }
    }
    return lps;
}

vector<int> kmp(string text, string pattern)
{
    vector<int> lps = buildLPS(pattern);
    vector<int> res;
    int tIdx = 0;
    int pIdx = 0;
    while (tIdx < text.size())
    {
        if (text[tIdx] == pattern[pIdx])
        {
            ++tIdx;
            ++pIdx;
            if (pIdx == pattern.size())
            {
                res.push_back(tIdx - pIdx);
                pIdx = lps[pIdx - 1];
            }
        }
        else
        {
            if (pIdx == 0)
            {
                ++tIdx;
            }
            else
            {
                pIdx = lps[pIdx - 1];
            }
        }
    }
    return res;
}