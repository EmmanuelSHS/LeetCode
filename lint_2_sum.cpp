/*************************************************************************
	> File Name: LINT_Sort_2_sum.cpp
	> Author: Mengqi Wang 
	> Created Time: Thu Nov  5 21:42:08 2015
 ************************************************************************/

#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {

        unordered_map<int, int> hash;
        vector<int> res;

        for (int i = 0; i < nums.size(); ++i) {
            if(hash.find(target - nums[i]) != hash.end()) {
                res.push_back(hash[target - nums[i]] + 1);
                res.push_back(i + 1);
                return res;
            }    
            hash[nums[i]] = i;
        }
    }
};

int main() {
    Solution *s = new Solution;
    int input[3] = {1, 0, -1};
    int target = -1;
    vector<int> in(input, input + sizeof(input)/sizeof(int));
    vector<int> out = s->twoSum(in, target);

    for (int i = 0; i < out.size(); ++i) cout << out[i] << endl;

    return 0;
}
