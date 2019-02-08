#include<bits/stdc++.h>
using namespace std;
string str;
int main() {
    for (int i=0; i<3;i++) {
        for (int j=0; j<3;j++) {
            if (i==j) {
                string str_tmp;
                cin >> str_tmp;
                str += str_tmp[i];
            }
        }
    }
    cout << str << endl;
    return 0;
}