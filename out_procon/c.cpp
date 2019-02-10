#include <bits/stdc++.h>
using namespace std;
int main() {
    int K, A, B;cin >> K >> A >> B;
    int sol = 0;
    if(B-A <=2) {
        cout << K+1;
    } else {
        if(K <= A){
            cout << K+1;
        } else {
            int diff = K-A+1;
            sol = A;
            if(diff % 2 == 0){
                sol = (K-B)*diff/2;
            } else {
                sol = (K-B)*(diff-1)/2+1;
            }
            cout << sol;
        }
    }
    return 0;
}
