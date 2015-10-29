/*************************************************************************
	> File Name: LINT_DP_lis.cpp
	> Author: Mengqi Wang
	> Created Time: Tue Oct 27 10:08:29 2015
	> Given two strings, find the longest common subsequence (LCS).
	Your code should return the length of LCS.
 ************************************************************************/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> nums) {
        int len = nums.size();
        int f[len];
        int f_max = 0;
        
        for (int i = 0; i < len; ++i) {
            // initialize
            f[i] = 1;
            // calculate
            // also could be divide-and-conquer
            for (int j = 0; j < i; ++j) {
                if (nums[i] >= nums[j] && f[i] < (f[j] + 1)) f[i] = f[j] + 1;
            }
            // compare
            if (f[i] > f_max) f_max = f[i];
        }
        
        return f_max;
    }
};

int main() {
    Solution *s = new Solution;
    int test[] = {4, 2, 4, 5, 3, 7};
    vector<int> input(test, test + sizeof(test)/sizeof(int));
    cout << s->longestIncreasingSubsequence(input) << endl;

    delete s;
    return 0;
}
