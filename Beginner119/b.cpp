#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int N;cin>>N;
    float sol=0;
    typedef pair<float, string> value_type;
    vector<value_type> v(N);
    for(int i=0;i<N;i++){
        cin >> v[i].first >> v[i].second;
    }
    for(int i=0;i<N;i++){
        if(v[i].second == "JPY"){
            sol += v[i].first;
        } else{
            sol += v[i].first * 380000.0;
        }
    }
    cout << sol << endl;
    return 0;
}