#include <bits/stdc++.h>
using namespace std;
int deg[10];
int main(void) {
    for(int i = 0;i<3;i++){
        int a, b;
        cin >> a >> b;
        a--; b--;
        deg[a]++;
        deg[b]++;
    }
    for(int i=0;i<4;i++) {
        if(deg[i] ==3) {
            cout << "NO" << endl;
        return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}