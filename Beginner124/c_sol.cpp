#include <bits/stdc++.h>
using namespace std;
int main()
{
    string S;
    cin >> S;
    int ans = S.size();
    for (int i = 0; i < 2; i++)
    {
        int cnt = 0;
        for (int j = 0; j < S.size(); j++)
        {
            if (j % 2 == 0 && S[j] != char(i + '0'))
                cnt++;
            if (j % 2 == 1 && S[j] == char(i + '0'))
                cnt++;
        }
        ans = min(ans, cnt);
    }
    cout << ans << endl;
    return 0;
}