/*************************************************************************
	> File Name: DP_Min_Imbalance.cpp
	> Author: Mengqi Wang 
	> Created Time: Thu Oct 15 00:51:24 2015
 ************************************************************************/

#include<cmath>
#include<iostream>
using namespace std;

#define MAX 100

int main() {
    // init
    int n = 9;
    int k = 2;
    int f[n + 1][k + 2];
    int a[n + 1];
    int sum[n + 1];
    int ave = 0;

    for (int i = 0;i < n + 1; ++i) {
        a[i] = i;
        sum[i] = sum[i - 1] + a[i];
    }
    ave = sum[n] / (k + 1);

    for (int i = 1; i < n + 1; ++i) {
        f[i][1] = abs(sum[i] - ave);
    }
    for (int j = 1; j < k + 2; ++j) {
        f[1][j] = abs(a[1] - ave);
    }
    
    // dp
    for (int i = 2; i < n + 1; ++i) {
        for (int j = 2; j < k + 2; ++j) {
            f[i][j] = MAX;
            for (int l = 1; l < i + 1; ++l) {
                int imb = max(f[l][j - 1], abs(sum[i] - sum[l] - ave));
                if (imb < f[i][j]) f[i][j] = imb;
            }
            //cout << f[i][j] << endl;
        }
    }

    cout << f[n][k + 1] << endl;
return 0;
}
