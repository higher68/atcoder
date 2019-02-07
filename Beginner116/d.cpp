#include <bits/stdc++.h>
#define FOR(i, begin, end) for(int i=(begin);i<(end);i++)
#define REP(i, n) FOR(i,0,n)
#define IFOR(i, begin, end) for(int i=(end)-1;i>=(begin);i--)
#define IREP(i, n) IFOR(i,0,n)
#define Sort(a) sort(a.begin(), a.end())
#define Reverse(a) reverse(a.begin(), a.end())
#define Lower_bound(v, x) distance(v.begin(), lower_bound(v.begin(), v.end(), x))
#define Upper_bound(v, x) distance(v.begin(), upper_bound(v.begin(), v.end(), x))
#define Max(a, b) a = max(a, b)
#define Min(a, b) a = min(a, b)
#define Ans(f, y, n) if(f) cout << y << endl; else cout << n << endl;
#define int long long
#define INF 1000000000000000000
using namespace std;
 
using vec = vector<int>;
using mat = vector<vec>;
using Pii = pair<int, int>;
using PiP = pair<int, Pii>;
using PPi = pair<Pii, int>;
using bools = vector<bool>;
 
template<typename T>
void readv(vector<T> &a){ REP(i, a.size()) cin >> a[i]; }
void readi(vector<int> &a){ REP(i, a.size()){cin >> a[i]; a[i]--;} }
template<typename T>
void debug(vector<vector<T>> m){ REP(i, m.size()){ REP(j, m[i].size()){ cout << m[i][j] << ","; } cout << endl;} }
 
 
 
signed main(){
    int N, K; cin >> N >> K;
    vec t(N), d(N);
    REP(i, N){
        cin >> t[i] >> d[i];
        t[i]--;
    }
    vector<Pii> p(N);
    REP(i, N) p[i] = Pii(d[i], t[i]);
    Sort(p); Reverse(p);
    
    int tmp = 0;
    vec cnt(N, 0);
    int v = 0;
    priority_queue<int, vector<int>, greater<int>> que;
    REP(i, K){
        tmp += p[i].first;
        cnt[p[i].second]++;
        if(cnt[p[i].second] >= 2) que.push(p[i].first);
        else v++;
    }
    int ans = tmp + v * v;
 
    FOR(i, K, N){
        if(que.empty()) break;
        if(cnt[p[i].second] >= 1) continue;
        cnt[p[i].second]++;
        int a = que.top(); que.pop();
        tmp -= a;
        tmp += p[i].first;
        v++;
        Max(ans, tmp + v * v);
    }
    cout << ans;
 
    return 0;
}