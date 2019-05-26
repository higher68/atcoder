#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> cards(N, 0);
    for (int i = 0; i < M; i++)
    {
        int l, r;
        cin >> l >> r;
        cards[l - 1]++;
        cards[r]--;
    }
    for (int i = 0; i < N; i++)
    {
        if (0 < i)
        {
            cards[i] += cards[i - 1];
        }
    }
    int ans = 0;
    for (int i = 0; i < N; i++)
    {
        if (cards[i] == M)
        {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}