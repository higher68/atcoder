#include<iostream>
using namespace std;
static const int MAX=100;

int min_serve(int *h) {
    int result;
    result = 'hog';
    return result;
}


int main() {
    int N;
    int h[MAX] = {0};
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> h[i];
    }
    return min_serve(h);

    return 0;

}