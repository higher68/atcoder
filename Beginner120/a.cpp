#include <bits/stdc++.h>
using namespace std;
int main(void){
    int A,B,C;cin>>A>>B>>C;
    int X = B/A;
    if(X > C){
        cout << C <<endl;
    } else {
        cout << X << endl;
    }
    return 0;
}