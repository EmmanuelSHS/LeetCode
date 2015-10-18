/*************************************************************************
	> File Name: LINT_DP_Coins_in_line.cpp
	> Author: 
	> Created Time: Sat Oct 17 21:53:51 2015
	> Question:
	> 	There are n coins in a line. Two players take turns to take one or two 	> coins from right side until there are no more coins left. The player who 		> take the last coin wins.
	>	Could you please decide the first play will win or lose?
	>	O(n) time and O(1) memory
 ************************************************************************/

#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    bool firstWillWin(int n) {
        // write your code here
        // fundamental hypothesis: 
        //      1st player keep the coins left to be odd
        //      2nd player keep the coins after he drawn to be even
        bool win = false;
        int i = 0;
        // a while loop decide the move of first player
        while (i < n) {
            // if 2 coins or 1 left, he wins
            if (i == (n - 1) || i == (n - 2)) return true;
            // else, 2 expected cases
            else {
                // if he faces even numbers, he would draw to make it odd,
                // which makes opponent draw 1 also to make it even
                if ((n - i) / 2 == 0) i += 2;
                // else he draw a two to keep it odd,
                // which makes opponent still draw 1
                else i += 3;
            }
        }
        return win;
    }
};

int main() {
    Solution *s = new Solution;
    int i = 0;
    cin >> i;
    cout << s->firstWillWin(i) << endl;
    
    delete s;

    return 0;
}
