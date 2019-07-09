#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N;
    cin >> N;
    vector<int> d(N);
    for (int i = 0; i < N; i++)
    {
        cin >> d[i];
    }
    int max_d = *max_element(d.begin(), d.end());
    vector<int> d_coun(max_d, 0);
    int d_sum = N;
    for (int i = 0; i < N; i++)
    {
        d_coun[d[i] - 1]++;
    }
    int ans = 0;
    for (int i = 0; i < max_d; i++)
    {
        d_sum -= d_coun[i];
        if (d_sum == N / 2)
        {
            ans++;
        }
    }
    cout << ans << endl;

    return 0;
}