/*************************************************************************
	> File Name: LINT_Sort_2_sum.cpp
	> Author: Mengqi Wang 
	> Created Time: Thu Nov  5 21:42:08 2015
 ************************************************************************/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> merge(vector<int> &left, vector<int> &right) {
        int n = left.size() + right.size();
        int sorted[n];
        int i = 0; int j = 0;
        for (int k = 0; k < n; ++k) {
            if (left[i] <= right[j]) {
                sorted[k] = left[i];
                ++i;
            }
            else {
                sorted[k] = right[j];
                ++j;
            }
        }
        return vector<int> (sorted, sorted + n/sizeof(int));
    }
    vector<int> Merge_sort(vector<int> &nums, int bgn, int end) {
        vector<int> sorted;
        if (bgn == end) return nums;
        else {
            int half = (bgn + end) / 2;
            vector<int> left = Merge_sort(nums, bgn, half);
            vector<int> right = Merge_sort(nums, half + 1, end);
            sorted = merge(left, right);
        }
        return sorted;
    }
    vector<int> twoSum(vector<int> &nums, int target) {
        // need to consider robusity under negative numbers in vector
        int n = nums.size();
        int *p = &nums[0]; 
        int *q = &nums[n - 1];
        int indice[2];
        
        vector<int> sorted = Merge_sort(nums, 0, n);
        while (true) {
            int sum = *p + *q;
            if (sum > target) --q;
            else if (sum < target) ++p;
            if (sum == target) break;
        }
    
        for (int i = 0; i < n; ++i) {
            if (nums[i] == *p) indice[0] = i + 1;
            if (nums[i] == *q) indice[1] = i + 1;
        }

        return vector<int> (indice, indice + sizeof(indice)/sizeof(int));
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
