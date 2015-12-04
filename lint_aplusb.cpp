/*************************************************************************
	> File Name: lint_bit_aplusb.cpp
	> Author: Mengqi Wang 
	> Created Time: Sun Nov 15 20:04:57 2015
    > adding two 32-bit int w/o using "+" operand
 ************************************************************************/

#include <iostream>
using namespace std;

class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) {
        // try to do it without arithmetic operators.
        int sum = a;
        int carry = b;
        
        while (carry) {
            int tmp = sum;
            
            // add w/o carry
            sum = tmp ^ carry;
            // record carry on i-th bit, add it into i-th bit
            carry = (tmp & carry) << 1;
        }
        return sum;
    }
};

int main() {
    int a = 100000000;
    int b = 200000000;

    Solution *s = new Solution;
    cout << s->aplusb(a, b) << endl;

return 0;
}

