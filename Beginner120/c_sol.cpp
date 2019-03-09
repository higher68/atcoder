#include <bits/stdc++.h>
using namespace std;
int main(void){
    string s;cin>>s;
    int s0=0, s1=0;
    for(int i=0;i<s.size();i++){
        if(s[i] == '0'){
            s0++;
        }else{
            s1++;
        }
    }
    cout << min(s0, s1)*2;
    return 0;
}