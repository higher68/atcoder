#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
    if (a < b)
    {
        swap(a, b);
    }
    if (b == 0)
    {
        return a;
    }
    return gcd(a % b, b);
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
    vector<int> S_pre, S_back;
    S_pre.push_back(A[0]);
    S_back.push_back(A[N - 1]);
    for (int i = 1; i < N; i++)
    {
        int tmp_pre = gcd(S_pre[i - 1], A[i]);
        int tmp_back = gcd(S_back[i - 1], A[N - 1 - i]);
        S_pre.push_back(tmp_pre);
        S_back.push_back(tmp_back);
    }
    reverse(S_back.begin(), S_back.end());
    //for (int i = 0; i < N; i++)
    //{
    //    cout << "S_pre:" << S_pre[i];
    //    cout << " S_back:" << S_back[i] << endl;
    //}
    vector<int> calc;
    calc.push_back(S_back[1]);
    for (int i = 1; i < N - 1; i++)
    {
        int tmp_calc = gcd(S_pre[i - 1], S_back[i + 1]);
        calc.push_back(tmp_calc);
    }
    calc.push_back(S_pre[N - 2]);
    //for (int i = 0; i < calc.size(); i++)
    //{
    //    cout << "calc:" << calc[i] << endl;
    //}
    int ans = *max_element(calc.begin(), calc.end());
    cout << ans << endl;
    return 0;
}