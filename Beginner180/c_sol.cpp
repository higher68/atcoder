#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
    // 2つの数が与えられた時のgcd
    // a > bと考える
    if (b == 0)
    {
        return a; // aの体力が残っている
    }
    else
    {
        gcd(b, a % b); // aがbで引かれまくって小さくなった方
    }
}

int gcd(vector<int> a)
{
    // 複数の数のgcdを求める
    int ans = a[0];
    for (int i = 1; i < a.size(); i++)
    {
        ans = gcd(ans, a[i]);
    }
    return ans;
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
    int ans = gcd(A);
    cout << ans << endl;
    return 0;
}