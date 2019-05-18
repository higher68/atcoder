#include <bits/stdc++.h>
using namespace std;
int main()
{
    string S;
    cin >> S;
    vector<int> cnt(2, 0);
    for (int i = 0; i < S.size(); i++)
    {
        cnt[S[i] - '0']++;
    }
    cout << min(cnt[0], cnt[1]) * 2 << endl;
    return 0;
}
