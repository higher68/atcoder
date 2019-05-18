#include <bits/stdc++.h>
using namespace std;
int main()
{
    string S;
    cin >> S;
    int s0 = 0, s1 = 0;
    for (int i = 0; i < S.size(); i++)
    {
        if (S[i] == '0')
        {
            s0++;
        }
        else
        {
            s1++;
        }
    }
    cout << min(s0, s1) * 2 << endl;
    return 0;
}
