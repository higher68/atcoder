#include <bits/stdc++.h>
using namespace std;
int main(void){
    int A, B, K;cin>>A>>B>>K;
    for(int i=min(A, B);i>0;i--){
        if(A % i == 0 && B % i == 0){
            --K;
            if(K == 0){
                cout << i << endl;
                return 0;
            }
        }
    }
}