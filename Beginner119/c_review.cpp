#include <bits/stdc++.h>
using namespace std;

int N, A, B, C;
vector<int> l(8);
int cost = 9999999;

int natural_num(int i)
{
    if (i < 0)
    {
        return 0;
    }
    else
    {
        return i;
    }
}

void calc(vector<int> v)
{
    int a = 0, b = 0, c = 0;
    int A_hight = 0, B_hight = 0, C_hight = 0;
    for (int i = 0; i < v.size(); i++)
    {
        // aggregate l to a, b, c
        if (v[i] == 0)
        {
            A_hight += l[i];
            a++;
        }
        else if (v[i] == 1)
        {
            B_hight += l[i];
            b++;
        }
        else if (v[i] == 2)
        {
            C_hight += l[i];
            c++;
        }
    }
    // calculate cost
    if (a != 0 & b != 0 & c != 0)
    {
        int da = natural_num(a - 1) * 10;
        int db = natural_num(b - 1) * 10;
        int dc = natural_num(c - 1) * 10;
        da += abs(A - A_hight);
        db += abs(B - B_hight);
        dc += abs(C - C_hight);
        int cost_tmp = da + db + dc;
        // cout << "cost" << cost_tmp << endl;
        if (cost_tmp < cost)
        {
            cost = cost_tmp;
        }
    }
}

void dfs(int depth, vector<int> v)
{
    if (depth == N)
    {
        calc(v);
        return;
    }
    for (int i = 0; i < 4; i++)
    {
        v[depth] = i;
        dfs(depth + 1, v);
    }
}

int main(void)
{
    cin >> N >> A >> B >> C;
    for (int i = 0; i < N; i++)
    {
        cin >> l[i];
    }
    vector<int> v(N, 0);
    dfs(0, v);
    cout << cost << endl;
    return 0;
}