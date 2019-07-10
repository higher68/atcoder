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
    sort(d.begin(), d.end());
    int d_right = d[N / 2];
    int d_left = d[N / 2 - 1];
    int ans = d_right - d_left;
    cout << ans << endl;
    return 0;
}