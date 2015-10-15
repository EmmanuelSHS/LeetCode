/*************************************************************************
	> File Name: DP_longest_com_subseq.cpp
	> Author: 
	> Mail: 
	> Created Time: Sun Oct 11 13:29:37 2015
 ************************************************************************/

#include<string>
#include<iostream>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string A, string B) {
        // write your code here
        int row = A.length() + 1;
        int col = B.length() + 1;
        int lcs[row][col];
        // DP for lcs
        for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (i == 0 || j == 0) {
                // init
                lcs[i][j] = 0;
            } else if (A[i - 1] == B[j - 1]) {
                /* 
                 * why judging by previous ?
                 * It's not "previous", by substitue i = 1 you will get that
                 */
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
            } else {
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
            }
        }
        }
        return lcs[row - 1][col - 1];
    };
};

int main() {
    Solution *s = new Solution;

    string A = "guurdbaxypvwotateuursrhqnzqeqk";
    string B = "qktmyfzeyelbckekldbbhrgbnpzqwo";

    cout << s->longestCommonSubsequence(A, B) << endl;

    delete s;

return 0;
}
