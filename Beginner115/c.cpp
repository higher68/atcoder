#include<iostream>
#include<algorithm>
using namespace std;
int main() {
  int N, K;
  cin >> N >> K;
  int h[N];
  for (int i = 0; i < N; i++) cin >> h[i];
  sort(h, h + N); // sortは引数に先頭と末尾のポインタを指定する
  int m = 1000000000;
  // cout << "hoge\n";
  for (int i = 0; i < N-K+1; i++) {
    m = min(m, h[i+K-1] - h[i]);
  }
  cout << m << endl;
}  

