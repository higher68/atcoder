#include <bits/stdc++.h>
using namespace std;
int N;
int A_min;
int A[100000];
int sol_min() {
    for(int i=0;i<N;i++){
        int hoge=A[i] % A_min;
        if(hoge !=0 && hoge < A_min){
            A_min=hoge;
            sol_min();
            return 0;
        }
    }
    return 0;
}
int main(void) {
    cin>>N;
    for(int i=0;i<N;i++) {
        cin >> A[i];
        // cout << A[i] << endl;
    }
    sort(A, A+N);
    A_min=A[0];
    sol_min(); 
    cout << A_min;
    return 0;
}