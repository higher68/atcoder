#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long N, A, B, C, D, E;
    cin >> N >> A >> B >> C >> D >> E;
    long long bot = min({A, B, C, D, E});
    long long min_path;
    min_path = 5 + (N + bot - 1) / bot - 1;
    cout << min_path << endl;
    return 0;
}