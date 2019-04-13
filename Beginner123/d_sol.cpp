#include <bits/stdc++.h>
using namespace std;
int main()
{
    int X, Y, Z, K;
    cin >> X >> Y >> Z >> K;
    vector<long long> A(X), B(Y), C(Z);
    for (int i = 0; i < X; i++)
    {
        cin >> A[i];
    }
    for (int i = 0; i < Y; i++)
    {
        cin >> B[i];
    }
    for (int i = 0; i < Z; i++)
    {
        cin >> C[i];
    }
    vector<long long> AB;
    for (int i = 0; i < X; i++)
    {
        for (int j = 0; j < Y; j++)
        {
            AB.push_back(A[i] + B[j]);
        }
    }
    sort(AB.begin(), AB.end());
    reverse(AB.begin(), AB.end());
    vector<long long> ABC;
    for (int i = 0; i < min(K, (int)AB.size()); i++)
    {
        for (int j = 0; j < Z; j++)
        {
            ABC.push_back(AB[i] + C[j]);
        }
    }
    sort(ABC.begin(), ABC.end());
    reverse(ABC.begin(), ABC.end());
    for (int i = 0; i < K; i++)
    {
        cout << ABC[i] << endl;
    }
    return 0;
}