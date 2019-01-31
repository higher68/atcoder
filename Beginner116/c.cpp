#include<iostream>
using namespace std;
static const int MAX=100;
int h[MAX+1] = {0};
int sol = 0;

int min_serve(int start, int stop) {
    int result;
    bool all_one = true;
    int tmp_start1, tmp_start2;
    for(int i = start; i <= stop; i++) {
        if(h[i] > 0){
            tmp_start1 = i;
            break;
        }
    }
    cout <<  tmp_start1 << endl;
    tmp_start2 = tmp_start1;
    for(int i = tmp_start1; i <= stop;i++) {
        if(h[i] == 0){
            all_one = false;
            min_serve(tmp_start2, i-1);
            tmp_start2 = i + 1;
        }
    }
    cout << all_one;
    if(all_one ==true) {
        cout << 33333 << endl;
        for(int i = start; i <= stop; i++) {
            h[i] -= 1;
        }
        sol += 1;
        min_serve(start, stop);
    }
    return sol;
}

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> h[i];
    }
    return min_serve(0, N-1);

    return 0;
}