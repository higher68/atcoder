#include <bits/stdc++.h>
using namespace std;

int N,A,B,C;
int min_cost=1<<21;
int l[8];
int natural_num(int i){
    if(i < 0){
        return 0;
    } else {
        return i;
    }
}

void calc(vector<int> v){
    // cout << "calc" << endl;
    int a=0,b=0,c=0,i=-1;
    int A_sol=0,B_sol=0,C_sol=0;
    int cost=0;
    // 各枝での合体後のA,B,C候補を計算
    for(auto itr=v.begin();itr!=v.end();itr++){
        i++;
        // cout << i << endl;
        if(*itr == 0){
            a++;
            A_sol += l[i];
        } else if(*itr == 1){
            b++;
            B_sol += l[i];
        } else if(*itr ==2){
            c++;
            C_sol += l[i];
        }
    }
    if(a!=0 and b!=0 and c!=0){
        // 合体にかかるコストを計算
        cost += natural_num(a-1) * 10;
        cost += natural_num(b-1) * 10;
        cost += natural_num(c-1) * 10;
        // 差を計算
        cost += abs(A-A_sol);
        cost += abs(B-B_sol);
        cost += abs(C-C_sol);
        // costの最小値更新
        // cout << cost;
        if(cost < min_cost) min_cost=cost;
    }
}

int main(void) {
    cin>>N>>A>>B>>C;
    for (int i=0;i<N;i++){
        cin>>l[i];
    }
    vector<int> v(N);
    for(int i=0;i<2<<(N*2);i++){
        for(int k=0;k<N;k++){
            v[k]=i>>2*k & 3;
        }
        calc(v);
    }
    cout << min_cost;
    return 0;
}