#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;
    vector<int> Nums;
    int flag = 1;
    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        if (S[i] == (char)('0' + flag))
        {
            cnt++;
        }
        else
        {
            Nums.push_back(cnt);
            cnt = 1;
            flag = 1 - flag;
        }
    }
    if (cnt != 0)
    {
        Nums.push_back(cnt);
    }
    // 配列のサイズが偶数じゃなかった場合、端っこの処理がめんどくさい
    // 端っこに一個足すと良い
    if (Nums.size() % 2 == 0)
    {
        Nums.push_back(0);
    }
    // cout << "complete" << endl;
    // Kの値に応じてどこまで見れるか
    // K=0だったら1、K=1だったら3、etc
    // for (int i = 0; i < Nums.size(); i++)
    // {
    //     cout << i << "th:" << Nums[i] << endl;
    // }
    int RANGE = 2 * K + 1;
    int tmp = 0;
    int left = 0;
    int right = 0;
    int ans = 0;
    for (int i = 0; i < Nums.size(); i += 2)
    {
        int Nextleft = i;
        int Nextright = min(i + RANGE, (int)Nums.size());

        while (Nextleft > left)
        {
            tmp -= Nums[left];
            left++;
        }
        while (Nextright > right)
        {
            tmp += Nums[right];
            right++;
        }
        ans = max(ans, tmp);
    }

    cout << ans << endl;
    return 0;
}