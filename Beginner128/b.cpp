#include <bits/stdc++.h>
using namespace std;
typedef pair<string, int> P;

bool pairCompare(const P &firstElof, const P &secondElof)
{
    return firstElof.second > secondElof.second;
}

int main()
{
    int N;
    cin >> N;
    vector<P> rest(N), ind(N);
    for (int i = 0; i < N; i++)
    {
        cin >> rest[i].first >> rest[i].second;
        ind[i].first = rest[i].first;
        ind[i].second = rest[i].second;
    }
    sort(rest.begin(), rest.end());
    // for (int i = 0; i < N; i++)
    // {
    //     cout << rest[i].first << ":" << rest[i].second << endl;
    // }
    for (int i = 1; i < N; i++)
    {
        if (rest[i - 1].first == rest[i].first)
        {
            int j = 0;
            while (j < rest.size() - i)
            {
                if (rest[i - 1 + j].first != rest[i + j].first)
                {
                    break;
                }
                else
                {
                    j++;
                }
            }
            // cout << "num:" << j << endl;
            sort(rest.begin() + i - 1, rest.begin() + i + j, pairCompare);
            i += j;
        }
    }
    //cout << "--------------------" << endl;
    //for (int i = 0; i < N; i++)
    //{
    //    cout << rest[i].first << ":" << rest[i].second << endl;
    //}
    for (int i = 0; i < N; i++)
    {
        int ans;
        for (int j = 0; j < N; j++)
        {
            if (rest[i].first == ind[j].first &
                rest[i].second == ind[j].second)
            {
                ans = j + 1;
                break;
            }
        }
        cout << ans << endl;
    }
    return 0;
}