#include <bits/stdc++.h>
using namespace std;
int solve_time(int a)
{
    if (a % 10 != 0)
    {

        return a + 10 - a % 10;
    }
    else
    {
        return a;
    }
    return 0;
}
int main()
{
    vector<int> ans;
    int a[5];
    for (int i = 0; i < 5; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (j != i)
            {
                for (int k = 0; k < 5; k++)
                {
                    if (k != i and k != j)
                    {
                        for (int l = 0; l < 5; l++)
                        {
                            if (l != i and l != j and l != k)
                            {
                                for (int m = 0; m < 5; m++)
                                {
                                    if (m != i and m != j and m != k and m != l)
                                    {
                                        int t_sum = 0;
                                        t_sum += solve_time(a[i]);
                                        t_sum += solve_time(a[j]);
                                        t_sum += solve_time(a[k]);
                                        t_sum += solve_time(a[l]);
                                        t_sum += a[m];
                                        ans.push_back(t_sum);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    int min = *min_element(ans.begin(), ans.end());
    cout << min;
    return 0;
}