#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int N, M;cin>>N>>M;
    vector<int> cnt(M, 0);
    for(int i=0;i<N;i++){
        int K;cin>>K;
        for(int j=0;j<K;j++){
            int a;cin>>a;a--;
            ++cnt[a];
        }
    }
    int sol=0;
    for(int i=0;i<M;i++){
        if(cnt[i] == N) {
            ++sol;
        }
    }
    cout << sol;
    return 0;
}