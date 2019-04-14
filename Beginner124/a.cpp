#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A, B;
    int ans[3];
    cin >> A >> B;
    ans[0] = A * 2 - 1;
    ans[1] = A + B;
    ans[2] = B * 2 - 1;
    cout << max({ans[0], ans[1], ans[2]}) << endl;
    return 0;
}