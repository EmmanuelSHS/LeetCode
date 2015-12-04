/*************************************************************************
	> File Name: Bit_Single_Number.cpp
	> Author: Mengqi Wang 
	> Created Time: Sun Oct 11 13:27:04 2015
    > Description: Given an array of integers, 
    >              every element appears twice except for one. 
    >              Find that single one.
 ************************************************************************/

#include<vector>
#include<iostream>
using namespace std;

class Solution {
    public:
    int singleNumber(vector<int>& nums) {
               int res = 0;
        // bit calculation
        for (int i = 0; i < nums.size(); ++i) {
                       res ^= nums[i];
        } 
               return res;
    }
};

int main() {
    Solution *s = new Solution;
    int input[] = {1,1,2,2,3,3,4,5,5};
    vector<int> test(input, input + sizeof(input)/sizeof(int));
    cout << s -> singleNumber(test) << endl;

    delete s;
}
