#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M; cin >>N >> M;
    int X[M];
    int ans=0;
    for (int i=0; i < M; i++) {
        cin >> X[i];
    }
   
    if (N >= M) {
        cout << 0;
    } else {
        sort(X.begin(), X.end());
        int dist[M-1];
        for (int i=0; i< M-1;i++){
            dist[i] = X[i+1] - X[i];
        }
        sort(dist.begin(), dist.end());
        for (int i=N-1;i < length(dist); i++) {
            ans += dist[i];
        }
        cout << ans;
    }
    return 0;
}