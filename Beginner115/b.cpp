#include<algorithm>
#include<iostream>
using namespace std;
int main() {
  int N;
  cin >> N;
  int S=0, M=0;
  for (int i = 0; i < N; ++i) {
    int p;
    cin >> p;
    S += p;
    M = max(M, p); // 大きい方を出力する
  }
  int ans = S - M / 2;
  cout << ans << endl; // endlはバッファをフラッシュする\nと同じ?
}

