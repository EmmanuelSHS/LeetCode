/*************************************************************************
	> File Name: dynamic_max_subarray.cpp
	> Author: 
	> Mail: 
	> Created Time: Sat Oct 10 16:24:23 2015
 ************************************************************************/

#include<iostream>
using namespace std;

#define ANEG -10000;

int max(int left, int right) {
    if (left >= right) return left;
    return right;
}

int main() {
    int n = 0;
    cin >> n;
    int a[n + 1];
    int b[n + 1];
    int m = ANEG;
    a[0] = 0; b[0] = 0;
    for (int i = 1; i < n + 1; ++i) cin >> a[i];

    for (int i = 1; i < n + 1; ++i) {
        b[i] = max(b[i - 1] + a[i], a[i]);
        if (m < b[i]) m = b[i];
    }

    cout << m << endl;

return 0;
}
