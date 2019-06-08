#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<pair<string, int>, int>> a;
    for (int i = 1; i < N + 1; i++)
    {
        string S;
        int P;
        cin >> S >> P;
        P = -P; // sortは昇順なので、降順にするために-1かける
        a.push_back(make_pair(make_pair(S, P), i));
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < N; i++)
    {
        cout << a[i].second << endl;
    }
    return 0;
}