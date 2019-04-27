#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A, B, C;
    cin >> A >> B >> C;
    if (A > B)
    {
        if (B < C and C < A)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
    if (A < B)
    {
        if (A < C and C < B)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
    return 0;
}
