#include <bits/stdc++.h>
using namespace std;
int main(void){
    int A,B,K;cin>>A>>B>>K;
    vector<int>sol;
    int len = 0;
    for (int i=1;i<=100;i++){
        int X = A % i;
        int Y = B % i;
        if(X == 0 and Y == 0) {
            len++;
            sol.push_back(i);
        }
    }
    cout << sol[len-K]<< endl;
    return 0;
}