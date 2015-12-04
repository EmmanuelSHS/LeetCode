/*************************************************************************
	> File Name: LINT_DP_EditDistance.cpp
	> Author: Mengqi Wang 
	> Created Time: Sun Oct 18 22:46:39 2015
    > Question: Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
      You have the following 3 operations permitted on a word:
        Insert a character
        Delete a character
        Replace a character
 ************************************************************************/

#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

#define MAX 10000

class Solution {
public:    
    /**
     * @param word1 & word2: Two string.
     * @return: The minimum number of steps.
     */
    int minDistance(string word1, string word2) {
        // Wagner–Fischer algorithm for Edit Distance
        int row = word1.size() + 1;
        int col = word2.size() + 1;
        // the status is when pointer reached i & j (actually (i - 1), (j - 1) in A & B)
        // what is the min steps needed to edit it to the same
        int f[row][col];

        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                f[i][j] = 0;
            }
        }        
        // marginal condition
        // if A[i] = B[0(1)], we need to insert to B to make it match together with the same subscript
        for (int i = 0; i < row; ++i) f[i][0] = i;
        // samely for deleting A
        for (int j = 0; j < col; ++j) f[0][j] = j;

        for (int i = 1; i < row; ++i) {
            for (int j = 1; j < col; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    // if equal, just use the previous, no need for adjustment
                    f[i][j] = f[i - 1][j - 1];
                }
                else {
                    // else we have to determine which one is the smallest, by min among three values,
                    // all of which are the previous + a cost of editing
                    f[i][j] = min(min(f[i - 1][j - 1] + 1, f[i][j - 1] + 1), f[i - 1][j] + 1);
                }
            }
        }
        
        // return result
        return f[row - 1][col - 1];
    }
};

int main() {
    Solution *s = new Solution;
    string A = "mart"; string B = "karma";
    
    cout << s->minDistance(A, B) << endl;

    return 0;
}
