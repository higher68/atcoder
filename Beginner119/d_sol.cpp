#include <bits/stdc++.h>
using namespace std;

long binarysearch(vector<long>v, long x){
    long ok = 0;
    long ng = v.size()-1;
    while(abs(ok-ng) > 1){
        long mid = (ng + ok) / 2;
        if (v[mid] >= x){
            ng = mid;
        } else {
            ok = mid;
        }
    }
    return ok;
}

long calc(vector<long>s, vector<long>t, long x){
    vector<long>a, b;
    long min = 1e+18;
    for(int i=0;i<2;i++){
        if(i==0){
            a=s;b=t;
        } else{
            a=t;b=s;
        }
        for(int j=0;j<2;j++){
            long a_pos = binarysearch(a, x) + j;
            long ax = a[a_pos];
            //cout << endl << "ax"<<ax<<endl;
            for(int k=0;k<2;k++){
                long b_pos = binarysearch(b, ax) + k;
                long bx = b[b_pos];
                //cout << endl << "bx"<<bx<<endl;
                long d = abs(bx-x) + abs(ax-bx);
                //cout <<endl<< "abs(bx-x)"<<abs(bx-x) <<endl<< "abs(ax-bx)"<<abs(ax-bx)<<endl;
                //cout <<endl<< "d" << d << endl;
                if(d < min and d >0){
                    min = d;
                    // cout << "min" << min << endl;
                }
            }
        }
    }
    return min;
}

int main(void){
    long A, B, Q;cin>>A>>B>>Q;A+=2;B+=2;
    vector<long>s(A), t(B);
    long v;
    long x;
    s[0] = -1e+18;
    s[A-1] = 1e+18;
    for(long i=1;i<A-1;i++){
        cin>>s[i];
    }
    t[0] = - 1e+18;
    t[B-1] = 1e+18;
    for(long i=1;i<B-1;i++){
        cin>>t[i];
    }
    for(long i=0;i<Q;i++){
        cin >> x;
        v= calc(s, t, x);
        cout << v << endl;
    }
    return 0;
}