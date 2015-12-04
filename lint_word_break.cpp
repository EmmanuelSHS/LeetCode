/*************************************************************************
	> File Name: LINT_DP_word_break.cpp
	> Author: Mengqi Wang
	> Created Time: Wed Oct 28 09:36:17 2015
	> Question: Given a string s and a dictionary of words dict, determine if s 	can be break into a space-separated sequence of one or more dictionary words.
 ************************************************************************/

#include <unordered_set>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    bool wordBreak(string s, unordered_set<string> &dict) {
        // TODO: time efficiency optimization needed
        int n = s.length();
        bool f[n + 1];
        
        f[0] = true;
        for (int i = 1; i < n + 1; ++i) {
            f[i] = false;
            for (int j = i - 1; j >= 0; --j) {
                f[i] = f[j] && (dict.find(s.substr(j, i - j)) != dict.end());
                if (f[i]) break;
            }
        }
        return f[n];
    }
};

int main() {
    Solution *s = new Solution;
    unordered_set<string> dict;
    dict.insert("aaaa"); dict.insert("aaa");
    string test = "aaaaaaa";
    cout << s-> wordBreak(test, dict) << endl;

    delete s;
    return 0;
}
