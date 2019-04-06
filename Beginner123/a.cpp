#include <bits/stdc++.h>
using namespace std;
int judge(int p, int q)
{
    if (p >= q)
    {
        return p - q;
    }
    else
    {
        return q - p;
    }
}

int main()
{
    int ans = 0;
    int p[5], k;
    for (int i = 0; i < 5; i++)
    {
        cin >> p[i];
    }
    cin >> k;
    for (int i = 0; i < 5; i++)
    {
        for (int j = i; j < 5; j++)
        {
            if (i != j)
            {
                int jud = judge(p[i], p[j]);
                if (jud <= k)
                {
                    ans++;
                }
            }
        }
    }
    if (ans == 10)
    {
        cout << "Yay!";
    }
    else
    {
        cout << ":(";
    }
    return 0;
}