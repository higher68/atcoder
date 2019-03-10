#include <bits/stdc++.h>
using namespace std;
int main() {
    int N,M,C;cin>>N>>M>>C;
    int ans=0;
    vector<int>B(M);
    for(int i=0;i<M;i++){
        cin >> B[i];
    }
    int A;
    for(int i=0;i<N;i++){
        int sum = C;
        for(int i=0;i<M;i++){
            cin >> A;
            sum += A*B[i];
        }
        if (sum > 0) ans++;
    }
    cout << ans << endl;
    return 0;
}