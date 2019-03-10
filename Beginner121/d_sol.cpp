#include <bits/stdc++.h>
using namespace std;

long long calc(long long A){
    // 10^12　2進数だと40桁くらい
    long long ans = 0;
    if(A <= 0) return 0;
    // 4のときは、見るべき整数は0, 1, 2, 3, 4なので、
    // 5つの整数から見なければいけない.1たす
    A++;
    //i桁目の偶奇を調べる
    for (int i=0;i<50;i++)
    {
        // 0桁目・・周期2
        // 1桁め・・周期4
        // 2桁め・・周期8
        // なので、周期＝loopは1LLをbitshiftしたらもとまる
        long long loop = (1LL << (i + 1));
        // loopする回数*1が出てくる回数
        // 0からAで考えるので、Aまで並べたら、loopはA/loopぶん通過数
        //その中で、1周期でloop/2個1はでる(書いたらわかる)
        // 周期/2ぶん1は残るため
        // ちょうどループ回数に収まるところまで
        long long cnt = (A / loop) * (loop / 2);
        // 端数を考える。ただし、0の連続があるので、
        // -(loop/2)・・・0の個数ぶん引く
        cnt += max(0LL, (A % loop) - (loop / 2));
        if (cnt % 2 == 1){
            ans += 1LL << i;
        }
    }
    return ans;
}

int main() {
    long long A, B;cin>>A>>B;
    long long ans = calc(B) ^ calc(A-1);
    cout << ans << endl;
    return 0;
}