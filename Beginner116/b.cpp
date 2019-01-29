#include <iostream>
using namespace std;
static const int MAX = 1000000;

int a[MAX] = {0};

int func(int n) {
    if (n % 2 == 0) {
        return n / 2;
    } else {
        return 3 * n + 1;
    }
    return 0;
}

int main()
{
    int s;
    int a_tmp;
    cin >> s;
    a_tmp = s;
    a[a_tmp - 1] = 1;
    for (int i = 1; i <= MAX; i++) {
        a_tmp = func(a_tmp);
        if (a[a_tmp - 1] == 1) {
            cout << i + 1;
            break;
        } else {
            a[a_tmp - 1] = 1;
        }
    }
    return 0;
}