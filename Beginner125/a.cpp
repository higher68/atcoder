#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A, B, T;
    cin >> A >> B >> T;
    int coun = (T + 0.5) / A;
    int ans = B * coun;
    cout << ans << endl;
    return 0;
}