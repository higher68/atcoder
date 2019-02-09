#include <bits/stdc++.h>
using namespace std;
int main() {
    vector<pair<int, int>>  a(3);
    for(int i=0;i<3;i++) {
        int pre, back;
        cin >> pre >> back;
        if(pre > back) {
            a[i] = make_pair(back, pre);
        } else{
            a[i] = make_pair(pre, back);
        }
    }
    sort(a.begin(), a.end(), [](auto &left, auto &right) {return left.first < right.first;});
    for(int i=0;i<3;i++){
    //    cout << a[i].first << a[i].second << endl;
    }
    int posi = 1;
    int gone[4] = {0};
    gone[0] = 1;
    for(int i=0;i<3;i++) {
//        cout << posi << endl;
//        for (auto itr=a.begin();itr!=a.end();++itr){
//            cout << (*itr).first <<(*itr).second << endl;
//        }
        for(auto itr=a.begin();itr!=a.end();itr++) {
            if (posi == (*itr).first) {
                posi = (*itr).second;
                gone[posi-1] = 1;
                a.erase(itr);
                break;
            } else if(posi == (*itr).second) {
                posi = (*itr).first;
                gone[posi-1]=1;
                a.erase(itr);
                break;
            }
        }
    }
//    for (int i=0;i<4;i++){
//        cout << gone[i];
//    }
    int sol[4] = {1,1,1,1};
    if(posi == 4){
        if(equal(gone, gone+4, sol)){
            cout << "YES";
        }else{
            cout << "NO";
        }
    } else {
        cout << "NO";
    }
    return 0;
}