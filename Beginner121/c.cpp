#include <bits/stdc++.h>
using namespace std;
int main() {
    int N,M;cin>>N>>M;
    long long  ans =0;
    typedef pair<int,int>value_type;
    vector<value_type> X(N);
    for (int i=0;i<N;i++){
        cin>>X[i].first>>X[i].second;
    }
    //sort(X.begin(), X.end(), bind(&value_type::first, _1) < bind(&value_type::first, _2));
    sort(X.begin(), X.end());
    //for(int i =0;i<N;i++){
    //    cout << X[i].first <<':'<< X[i].second<<endl;
    //}
    while(M > 0){
        for(int i=0;i<N;i++){
            if(X[i].second > M){
                ans += (long long)X[i].first * M;
                M = 0;
            } else{
                ans +=(long long)X[i].first * X[i].second;
                M -= X[i].second;
            }
        }
    }
    cout << ans << endl;
    return 0;
}

