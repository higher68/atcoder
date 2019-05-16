#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    vector<int> S_l(Q), S_r(Q);
    for (int i = 0; i < Q; i++)
    {
        cin >> S_l[i] >> S_r[i];
        // S_l[i]--;
        // S_r[i]--;
    }
    vector<int> S_ind(1, 0);
    int i = 1;
    while (i < N + 1)
    {
        string S_part = S.substr(i - 1, 2);
        // cout << "str" << S_part << endl;
        if (S_part == "AC")
        {
            S_ind.push_back(S_ind[i - 1]);
            S_ind.push_back(S_ind[i] + 1);
            i += 2;
        }
        else
        {
            S_ind.push_back(S_ind[i - 1]);
            i++;
        }
    }
    //for (int i = 0; i < N + 1; i++)
    //{
    //    cout << i << "th" << S_ind[i] << endl;
    //}
    for (int i = 0; i < Q; i++)
    {
        int ans = 0;
        // cout << "S_r" << S_r[i] << endl;
        //cout << "S_l" << S_l[i] << endl;
        ans += S_ind[S_r[i]] - S_ind[S_l[i]];
        cout << ans << endl;
    }
    return 0;
}