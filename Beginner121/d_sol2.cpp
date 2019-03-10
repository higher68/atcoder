#include <bits/stdc++.h>
using namespace std;

long long calc(long long A){
    long long cnt1 = (A + 1) /2;
    long long ans = cnt1 % 2;
    if (A % 2 == 0) ans = A;
    return ans;
}

int main() {
    long long a, b;cin>>a>>b;
    long long ans = calc(b) ^ calc(a-1);
    cout << ans << endl;
    return 0;
}