#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int S;
    string S_tmp;
    for (int i=0;i<10;i++){
        char tmp;cin >> tmp;
        if (tmp!='/'){
            S_tmp += tmp;
        }
    }
    S = atoi(S_tmp.c_str());
    if (S <= 20190430){
        cout << "Heisei" << endl;
    } else {
        cout << "TBD" << endl;
    }
    return 0;
}