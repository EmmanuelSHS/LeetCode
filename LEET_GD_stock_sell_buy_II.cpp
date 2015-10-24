/*************************************************************************
	> File Name: LEET_GD_stock_sell_buy_II.cpp
	> Author: Mengqi Wang 
	> Created Time: Sat Oct 24 10:31:37 2015
    	> Say you have an array for which the ith element is the price of a given 		stock on day i.
		Design an algorithm to find the maximum profit. You may complete as 		many transactions as you like (ie, buy one and sell one share of the stock 		multiple times). However, you may not engage in multiple transactions at the 	same time (ie, you must sell the stock before you buy again).
 ************************************************************************/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        if (prices.size() > 0) {
            for (int i = 0; i < prices.size() - 1; ++i) {
                // sell if yesterday is less than today
                int diff = prices[i + 1] - prices[i];
                if (diff > 0) max += diff;
            }
        }
        return max;
    }
};

int main() {

    Solution *s = new Solution;
    int inp[5] = {1, 2, 3, 4, 5};
    vector<int> prices(inp, inp + sizeof(inp)/sizeof(int));
    cout << s->maxProfit(prices) << endl;
    return 0;
}
