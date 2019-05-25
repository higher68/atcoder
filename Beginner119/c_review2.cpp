#include <bits/stdc++.h>
using namespace std;

int N, A, B, C;
vector<int> l(8);
int min_cost = 99999999;

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
    int dA = 0, dB = 0, dC = 0;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i] == 0)
        {
            a++;
            dA += l[i];
        }
        else if (v[i] == 1)
        {
            b++;
            dB += l[i];
        }
        else if (v[i] == 2)
        {
            c++;
            dC += l[i];
        }
    }
    dA = abs(dA - A);
    dB = abs(dB - B);
    dC = abs(dC - C);
    if (a != 0 & b != 0 & c != 0)
    {
        dA += natural_num(a - 1) * 10;
        dB += natural_num(b - 1) * 10;
        dC += natural_num(c - 1) * 10;
        int cost = dA + dB + dC;
        min_cost = min(min_cost, cost);
    }
}

int main()
{
    cin >> N >> A >> B >> C;
    vector<int> v(N);
    for (int i = 0; i < N; i++)
    {
        cin >> l[i];
    }
    for (int i = 0; i < 2 << (N * 2); i++)
    {
        for (int k = 0; k < N; k++)
        {
            // 4進数なので2ビットずつ右シフト
            // 右端の値を取り出すので3=11bで論理積をとる
            v[k] = i >> 2 * k & 3;
        }
        calc(v);
    }
    cout << min_cost << endl;
    return 0;
}