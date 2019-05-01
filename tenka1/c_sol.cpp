#include <bits/stdc++.h>
using namespace std;
int main(void)
{
    int N;
    cin >> N;
    string S;
    cin >> S;
    // 累積和での実装
    vector<int> blacks(1, 0), whites(1, 0);
    for (int i = 0; i < N; i++)
    {
        if (S[i] == '#')
        {
            blacks.push_back(blacks[i] + 1);
        }
        else
        {
            blacks.push_back(blacks[i]);
        }
        if (S[N - 1 - i] == '.')
        {
            whites.push_back(whites[i] + 1);
        }
        else
        {
            whites.push_back(whites[i]);
        }
    }
    // 番兵を前後にくっつける
    blacks.push_back(blacks[N]);
    whites.push_back(whites[N]);
    reverse(whites.begin(), whites.end());
    vector<int> costs;
    for (int i = 0; i < N + 2; i++)
    {
        costs.push_back(blacks[i] + whites[i + 1]);
    }
    int ans = *min_element(costs.begin(), costs.end());
    //for (int i = 0; i < costs.size(); i++)
    //{
    //    cout << "blacks:" << blacks[i] << endl;
    //    cout << "whites:" << whites[i] << endl;
    //}
    cout << ans << endl;
    return 0;
}