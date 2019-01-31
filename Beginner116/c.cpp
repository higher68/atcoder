#include<iostream>
using namespace std;
static const int MAX=100;
int h[MAX] = {0};

int min_serve(int start, int stop) {
    int result;
    bool all_one = true;
    for(int i = start; i <= stop; i++) {
        if(h[i] == 0){
            all_one = false;
            break;
        }
    }
    if(all_one ==true) {
        for(int i = start; i <= stop; i++) {
            h[i] -= 1;
        }
    }

    return result;
}

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> h[i];
    }
    return min_serve(h);

    return 0;

}