#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;
    int l_max, r_min;
    cin >> l_max >> r_min;
    for (int i = 1; i < M; i++)
    {
        int l, r;
        cin >> l >> r;
        if (l > l_max)
        {
            l_max = l;
        }
        if (r < r_min)
        {
            r_min = r;
        }
    }
    int ans;
    if (r_min >= l_max)
    {
        ans = r_min - l_max + 1;
    }
    else
    {
        ans = 0;
    }
    cout << ans << endl;
    return 0;
}