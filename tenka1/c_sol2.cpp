#include <bits/stdc++.h>
using namespace std;
int main(void)
{
    int N;
    cin >> N;
    string S;
    cin >> S;
    // しゃくとり法
    vector<int> cost;
    int ans_tmp = 0;
    for (int i = 0; i < N; i++)
    {
        if (S[i] == '.')
        {
            ans_tmp++;
        }
    }
    cost.push_back(ans_tmp);
    for (int i = 1; i < N + 1; i++)
    {
        ans_tmp = cost[i - 1];
        if (S[i - 1] == '#')
        {
            ans_tmp++;
        }
        else
        {
            ans_tmp--;
        }
        cost.push_back(ans_tmp);
    }
    int ans = *min_element(cost.begin(), cost.end());
    cout << ans << endl;
    return 0;
}