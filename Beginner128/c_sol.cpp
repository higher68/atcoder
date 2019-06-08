#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> a(N); //スイッチのvector
    // input処理
    // 電球に関してループ
    for (int i = 0; i < M; i++)
    {
        int k;
        cin >> k;
        // 電球iと繋がっているスイッチの数でループ
        for (int j = 0; j < k; j++)
        {
            int s;
            cin >> s;
            s--;
            // 電球iが繋がっているs番のスイッチと繋がっている状態を
            // a[s]のi桁目のbitが1かで判断
            // 各スイッチについて、電球iと繋がっていれば1を
            // 繋がっていなければ0を入れる
            // 2進数の足し算は|=
            a[s] |= 1 << i;
        }
    }
    int P = 0;
    // 電球の数でループ
    for (int i = 0; i < M; i++)
    {
        int x;
        cin >> x;
        // i番目の電球が偶数回onなら0奇数回なら1として2進数作成
        P |= x << i;
    }
    // スイッチの押し方を全部試す
    // N=3で100なら、3番目のみおす
    // N=3で101なら3番目と1番目を押す。
    int ans = 0;
    for (int s = 0; s < (1 << N); s++)
    {
        int t = 0;
        // sの押し方をした時、それを作れるかチェック
        // 各スイッチでループ
        for (int i = 0; i < N; i++)
        {
            // i番めのスイッチがの時
            if (s >> i & 1)
            {
                // t状態にxorをかける
                // on*onなら0に、on*offなら1に
                t ^= a[i];
            }
        }
        // 最終的に想定している状態か判定
        if (t == P)
        {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}