#include <bits/stdc++.h>
using namespace std;
int tile_reverse(string A, char flag)
{
    int ans = 0;
    char tmp_flag = flag;
    if (A[0] != tmp_flag)
    {
        ans++;
    }
    for (int i = 1; i < A.size(); i++)
    {
        if (A[i] == tmp_flag)
        {
            ans++;
            if (A[i] == '0')
            {
                tmp_flag = '1';
            }
            else
            {
                tmp_flag = '0';
            }
        }
        else
        {
            tmp_flag = A[i];
        }
    }
    return ans;
}
int main()
{
    string S;
    cin >> S;
    int ans0, ans1;
    ans0 = tile_reverse(S, '0');
    ans1 = tile_reverse(S, '1');
    cout << min(ans0, ans1) << endl;
    return 0;
}