#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N;
    cin >> N;
    long long A, B, C, D, E;
    cin >> A >> B >> C >> D >> E;
    long long MinMove = min({A, B, C, D, E});
    long long ans = (N + MinMove - 1) / MinMove + 4;
    cout << ans << endl;
    return 0;
}