#include <bits/stdc++.h>
using namespace std;

int N, A, B, C;
vector<int> l(8);

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

int calc(vector<int> v)
{
    int a = 0, b = 0, c = 0;
    for (int i = 0; i < v.size(); i++)
    {
        // aggregate l to a, b, c
        if (v[i] == 0)
        {
            a += l[i];
        }
        else if (v[i] == 1)
        {
            b += l[i];
        }
        else if (v[i] == 2)
        {
            c += l[i];
        }
    }
    // calculate cost
    int da = natural_num(A - a);
    int db = natural_num(B - b);
    int dc = natural_num(C - c);
    int cost = da + db + dc;
}

int dfs(int depth, vector<int> v)
{
    if (depth == N)
    {
        calc(v);
    }
    if (depth == N)
    {
        return N;
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
    return 0;
}