#include <bits/stdc++.h>
using namespace std;
int main() {
    int H,W;cin>>H>>W;
    int h,w;cin>>h>>w;
    int sum=H*W;
    int gyo_dif = h*W;
    int retsu_dif = w*H;
    int hokan = h*w;
    int ans = sum - gyo_dif - retsu_dif + hokan;
    cout << ans << endl;
    return 0;
}