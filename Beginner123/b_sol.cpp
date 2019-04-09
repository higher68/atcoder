#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    vector<int> A(5);
    vector<int> B(5);
    for (int i = 0; i < 5; i++)
    {
        cin >> A[i];
        if (A[i] % 10 == 0)
        {
            B[i] = 0;
        }
        else
        {
            B[i] = 10 - A[i] % 10;
        }
    }
    // 添え字取得
    vector<int>::iterator max = max_element(B.begin(), B.end());
    size_t max_index = distance(B.begin(), max);
    int sol = 0;
    // 待ち時間は、どの注文する順番で頼んでも、同じ時間かかる
    // 理由としては、結局10秒の倍数だけ待つため
    // ただ、その中で一つだけ待たなくてもいいものを作る場合、
    // 待ち時間が最大のものを選んだら良い
    for (int i = 0; i < 5; i++)
    {
        if (i != max_index)
        {
            if (A[i] % 10 == 0)
            {
                sol += A[i];
            }
            else
            {
                sol += A[i] + 10 - A[i] % 10;
            }
        }
        else
        {
            sol += A[i];
        }
    }
    cout << sol;
    return 0;
}