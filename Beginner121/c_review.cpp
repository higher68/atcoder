#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;
    vector<pair<int, int>> A(N);
    for (int i = 0; i < N; i++)
    {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        A[i].first = tmp1;
        A[i].second = tmp2;
    }
    //for (int i = 0; i < N; i++)
    //{
    //    cout << i << "th" << A[i].first << endl;
    //}
    sort(A.begin(), A.end());
    //    for (int i = 0; i < N; i++)
    //    {
    //        cout << i << "th" << A[i].first << endl;
    //    }
    //    reverse(A.begin(), A.end());
    //    for (int i = 0; i < N; i++)
    //    {
    //        cout << i << "th" << A[i].first << endl;
    //    }
    int i = -1;
    long long cnt = 0;
    while (M > 0)
    {
        i++;
        int M_tmp = M;
        M_tmp -= A[i].second;
        if (M_tmp <= 0)
        {
            cnt += (long long)M * A[i].first;
        }
        else
        {
            cnt += (long long)A[i].second * A[i].first;
        }
        M -= A[i].second;
    }
    cout << cnt << endl;
    return 0;
}