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
    sort(A.begin(), A.end());
    reverse(A.begin(), A.end());
    sort(B.begin(), B.end());
    reverse(B.begin(), B.end());
    sort(C.begin(), C.end());
    reverse(C.begin(), C.end());
    vector<long long> ABC;
    for (int a = 0; a < X; a++)
    {
        for (int b = 0; b < Y; b++)
        {
            if ((a + 1) * (b + 1) > K)
            {
                break;
            }
            for (int c = 0; c < Z; c++)
            {
                if ((a + 1) * (b + 1) * (c + 1) > K)
                {
                    break;
                }
                ABC.push_back(A[a] + B[b] + C[c]);
            }
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