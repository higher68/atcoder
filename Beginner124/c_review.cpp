#include <bits/stdc++.h>
using namespace std;
int main()
{
    string S;
    cin >> S;
    int white = 0;
    int black = 0;
    // cout << S.size() << endl;
    for (int i = 0; i < S.size(); i++)
    {
        if (i % 2 == 0)
        {
            if (S[i] == '1')
            {
                white++;
            }
            else
            {
                black++;
            }
        }
        else
        {
            if (S[i] == '1')
            {
                black++;
            }
            else
            {
                white++;
            }
        }
    }
    // cout << black << white << endl;
    cout << min(black, white) << endl;
    return 0;
}