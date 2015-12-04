/*************************************************************************
	> File Name: LINT_DP_Backpack.cpp
	> Author: Mengqi Wang 
	> Created Time: Fri Oct 16 18:48:35 2015
 ************************************************************************/

#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

#define MAX 1000
int f[MAX][MAX];
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        int len = A.size();
        bool f[m + 1];
        for (int i = 0; i < m + 1; ++i) f[i] = false;
        f[0] = true;
        
        for (int i = 0; i < len; ++i) {
            for (int j = m; j >= A[i]; --j) {
                f[j] = f[j] || f[j - A[i]];
            }
        }
    
        for (int i = m; i >= 0; --i) {
            if (f[i]) return i;
        }
    }
};

int main() {
    int m = 10;
    int a[] = {3, 4, 8, 5};
    vector<int> A(a, a + sizeof(a)/sizeof(int));
    Solution *s = new Solution;
    cout << s->backPack(m, A) << endl;
    delete s;

    return 0;
}
