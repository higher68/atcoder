#include<iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int L[N];
    int sum = 0;
    int mx = 0;
    for (int i=0;i < N;i++) {
        cin >> L[i];
        if (L[i] > L[mx]) {
            mx = i;
        }
    }
    for (int i=0;i < N;i++){
        if (i != mx) {
            sum += L[i];
        }
    }
    if (sum > L[mx]) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}