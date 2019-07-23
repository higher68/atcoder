#include <bits/stdc++.h>
using namespace std;

double calc(vector<int> y, vector<int> z)
{
    int sum = 0;
    for (int i = 0; i < y.size(); i++)
    {
        sum += (y[i] - z[i]) * (y[i] - z[i]);
    }
    return sqrt(double(sum));
}

int main()
{
    int N, D;
    cin >> N >> D;
    vector<vector<int>> X(N);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < D; j++)
        {
            int x;
            cin >> x;
            X[i].push_back(x);
        }
    }
    int ans = 0;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            double tmp_dist = calc(X[i], X[j]);
            double tmp_dist2 = double(floor(tmp_dist));
            if (tmp_dist == tmp_dist2)
            {
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}