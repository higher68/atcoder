#include <bits/stdc++.h>
using namespace std;

int func(int i)
{
    vector<int> A{2, 5, 5, 4, 5, 6, 3, 7, 6};
    return A[i - 1];
}

int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> A(M);
    for (int i = 0; i < M; i++)
    {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    // for (int i = 0; i < M; i++)
    // {
    //     cout << A[i];
    // }
    vector<int> dp(N, -10000000);
    dp[0] = 0;
    for (int i = 1; i < N; i++)
    {
        int mx = -100000000;
        for (int j = 0; j < M; j++)
        {
            if (i - func(A[j]) >= 0)
            {
                int mx2 = dp[i - func(A[j])] + 1;
                mx = max(mx, mx2);
            }
            //cout << "mx" << mx << endl;
            dp[i] = mx;
        }
        //cout << "dp[i]" << dp[i] << endl;
    }
    string ans = "";
    for (int i = 0; i < N; i++)
        //{
        //    cout << i << "dp[i]" << dp[i] << endl;
        //}
        for (int i = N - 1; i > 1; i--)
        {
            for (int j = M - 1; j > 0; j--)
            {
                if (dp[i - func(A[j])] == dp[i] - 1)
                {
                    //cout << A[j] << endl;
                    ans += to_string(A[j]);
                    //cout << ans << endl;
                    break;
                }
            }
        }
    cout << ans << endl;
    return 0;
}