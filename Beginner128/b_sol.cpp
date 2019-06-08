#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<tuple<string, int, int>> a;
    for (int i = 1; i < N + 1; i++)
    {
        string S;
        int P;
        cin >> S >> P;
        P = -P; // sortは昇順なので、降順にするために-1かける
        a.push_back(tie(S, P, i));
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < N; i++)
    {
        cout << get<2>(a[i]) << endl;
    }

    return 0;
}