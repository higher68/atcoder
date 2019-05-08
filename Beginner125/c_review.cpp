#include <bits/stdc++.h>
using namespace std;
int gcd(int a, int b)
{
    if (a > b)
    {
        swap(a, b);
    }
    if (a != 0)
    {
        return gcd(b % a, a);
    }
    else
    {
        return b;
    }
}
int main()
{
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    vector<int> left_sum(N), right_sum(N);
    left_sum[0] = A[0];
    right_sum[0] = A[N - 1];
    for (int i = 1; i < N; i++)
    {
        left_sum[i] = gcd(left_sum[i - 1], A[i]);
        right_sum[i] = gcd(right_sum[i - 1], A[N - i - 1]);
    }
    reverse(right_sum.begin(), right_sum.end());
    // for (int i = 0; i < N; i++)
    // {
    //     cout << "left_sum" << left_sum[i] << endl;
    //     cout << "right_sum" << right_sum[i] << endl;
    // }
    vector<int> calc(N);
    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            calc[0] = right_sum[1];
        }
        else if (i == N - 1)
        {
            calc[N - 1] = left_sum[N - 2];
        }
        else
        {
            calc[i] = gcd(left_sum[i - 1], right_sum[i + 1]);
        }
    }
    int ans = *max_element(calc.begin(), calc.end());
    //for (int i = 0; i < N; i++)
    //{
    //    cout << "calc" << calc[i] << endl;
    //}
    cout << ans << endl;
    return 0;
}