#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int a[5];
    int k;
    for (int i = 0; i < 5; i++)
    {
        cin >> a[i];
    }
    cin >> k;
    // 今回はa<b<c<・・・<e
    // 最大値であるaとeの距離がk以下ならok
    if (a[0] - a[4] <= k and a[0] - a[4] >= -k)
    {
        cout << "Yay!";
    }
    else
    {
        cout << ":(";
    }
    return 0;
}