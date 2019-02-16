#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int N, M; cin >> N >> M;
    int A[30][30] = {0};
    int sol=0;
    for(int i=0;i<N;i++) {
        int K;cin >> K;
        for(int j=0;j<K;j++){
            int magic; cin>>magic;magic--;
            A[i][magic]=1;
        }
    }
    for(int i=0;i<M;i++){
        int judge=0;
        for(int j=0;j<N;j++){
            if(A[j][i]==0){
                judge=1;
                break;
            }
        }
        if(judge==0){
            sol++;
        }
    }
    cout << sol;
    return 0;
}