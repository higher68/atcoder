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
        sort(X, X+M);
        int dist[M-1];
        for (int i=0; i< M-1;i++){
            dist[i] = X[i+1] - X[i];
            // cout << i << dist[i] << endl;
        }
        sort(dist, dist+M-1, greater<>());
        for (int i=N-1;i < sizeof(dist)/sizeof(*dist); i++) {
            ans += dist[i];
        }
        cout << ans << endl;
    }
    return 0;
}