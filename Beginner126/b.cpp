#include <bits/stdc++.h>
using namespace std;
int main()
{
    string S;
    cin >> S;
    int S_left = atoi(S.substr(0, 2).c_str());
    int S_right = atoi(S.substr(2, 2).c_str());
    bool left_judge_m = (1 <= S_left) and (S_left <= 12);
    bool left_judge_y = 0 <= S_left;
    bool right_judge_m = (1 <= S_right) and (S_right <= 12);
    bool right_judge_y = 0 <= S_right;
    bool mmyy = left_judge_m & right_judge_y;
    bool yymm = left_judge_y & right_judge_m;
    if (mmyy == true and yymm == true)
    {
        cout << "AMBIGUOUS" << endl;
    }
    else if (mmyy == true and yymm == false)
    {
        cout << "MMYY" << endl;
    }
    else if (mmyy == false and yymm == true)
    {
        cout << "YYMM" << endl;
    }
    else
    {
        cout << "NA" << endl;
    }
    return 0;
}