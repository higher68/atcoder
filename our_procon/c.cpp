#include <bits/stdc++.h>
using namespace std;
int main() {
    long K, A, B;cin >> K >> A >> B;
    long sol = 0;
    if(B-A <=2) {
        cout << K+1;
    } else {
        if(K <= A){
            cout << K+1;
        } else {
            long diff = K-A+1;
            sol = A;
            if(diff % 2 == 0){
                sol += (B-A)*diff/2;
            } else {
                sol += (B-A)*(diff-1)/2+1;
            }
            cout << sol;
        }
    }
    return 0;
}
