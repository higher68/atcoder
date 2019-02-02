#include<iostream>
using namespace std;

int main() {
    int n;
    int ans = 0;
    int active = 0;
    cin >> n;
    int h[n];
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    for (int i = 0; i < n; i++) {
        if (active >= h[i]) {
            active = h[i];
        } else {
            ans += h[i] - active;
            active = h[i];
        }
    }
    cout << ans;
    return 0;
}