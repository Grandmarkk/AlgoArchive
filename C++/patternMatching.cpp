#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

/**
 * @brief The Longest Prefix Suffix array
 *
 * @param pattern a string
 * @return an int vector lps, lps[i] represent the length of the longest proper prefix and suffix at pattern[i]
 * @note use with kmp()
 */
vector<int> buildLPS(string &pattern)
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

/**
 * @brief Search the occurence of pattern in the text
 *
 * @param text the haystack
 * @param pattern the needle
 */
vector<int> kmp(string &text, string &pattern)
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

/**
 * @brief Gusfield's Z-Algorithm
 * @param text a string
 * @return an array of z values, the length of the longest substring at each position that matches the prefix of text
 */
vector<int> buildZ(string &text)
{
    int len = text.size();
    vector<int> zVals(len, 0);
    int l = 0, r = 0;
    for (int i = 1; i < len; ++i)
    {
        // Within Z-box
        if (i <= r)
        {
            zVals[i] = min(r - i + 1, zVals[i - l]);
        }
        // Compare explicitly
        while (i + zVals[i] < len && text[zVals[i]] == text[i + zVals[i]])
        {
            ++zVals[i];
        }
        // Update Z-box bounds
        if (i + zVals[i] - 1 > r)
        {
            l = i;
            r = i + zVals[i] - 1;
        }
    }
    return zVals;
}

/**
 * @brief Build the R value matrix.
 * m[i] is a map storing the right most occurence of each char upto text[i]
 * @param pattern a string
 * @return R matrix, a vector of a hash map
 * @note used for bad character rule in BM
 */
vector<unordered_map<char, int>> buildR(string &pattern)
{
    int len = pattern.size();
    vector<unordered_map<char, int>> rm;
    unordered_map<char, int> cur;

    rm.push_back(cur);

    for (int i = 1; i < len; i++)
    {
        cur[pattern[i - 1]] = i - 1;
        rm.push_back(cur);
    }

    return rm;
}

/**
 * @brief Build the good suffix table
 * @param pattern a string
 * @return an int vector containing the good suffix values
 * @note used for good suffix rule for BM
 */
vector<int> buildGS(string &pattern)
{
    // Build Z-suffix array
    reverse(pattern.begin(), pattern.end());
    vector<int> zs = buildZ(pattern);
    reverse(zs.begin(), zs.end());

    // Build good suffix array
    int len = pattern.size();
    vector<int> gs(len + 1, -1);

    for (int i = 0; i < len - 1; i++)
    {
        int j = len - zs[i];
        gs[j] = i;
    }

    return gs;
}