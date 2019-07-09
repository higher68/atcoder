#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    int ans = 0;
    for (int i = 1; i < n - 1; i++)
    {
        vector<int> check(3);
        check = {p[i - 1], p[i], p[i + 1]};
        sort(check.begin(), check.end());
        if (check[1] == p[i])
        {
            ans++;
        }
    }
    cout << ans;
    return 0;
}