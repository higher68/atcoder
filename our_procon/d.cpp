#include <bits/stdc++.h>
using namespace std;

void chmin(int& a, int b) {
    a = min(a, b);
}

int main(void) {
    int L;cin>>L;
    int A[L];
    for (int i=0;i<L;i++) cin>>A[i];
    int dp[L+1][5];
    for(int i=0;i<=L;i++) for(int j=0;j<5;j++) dp[i][j]=1e9;
    dp[0][0] = 0;
    for(int i=0;i<L;i++) {
        int pre=dp[i][0];
        int diff;
        for(int j=0;j<5;j++){
            // 遷移元の最小を探す。この書き方だと、preのjは求めるj以下に必ずなる
            chmin(pre, dp[i][j]);
            if(j==0 || j==4) {
                diff = A[i];
            } else if(j==1 || j==3) {
                diff = (A[i]==0 ? 2 : A[i]%2);
            } else {
                diff = (A[i]+1)%2;
            }
            chmin(dp[i+1][j], pre+diff);
        }
    }
    int ans = dp[L][0];
    for(int j=1;j<5;j++) chmin(ans, dp[L][j]);
    cout << ans;
    return 0;
}