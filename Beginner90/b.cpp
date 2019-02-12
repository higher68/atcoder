#include<bits/stdc++.h>
using namespace std;
int main(void) {
    int A, B; cin >>A >> B;
    int count = 0;
    for(int i=0;i<10;i++) {
        int candi=i*10000 + i * 1000+i*100+i*10+i;
        if(A <= candi and candi <= B) {
            count += 1
        }
    }
    for(int i=0;i<10;i++) {
        for (j 0;j<1;j++){
            if (i != j){
                int candi = i*10000 + j * 1000+i*100+i*10+i;
                if(A <= candi and candi <= B) {
                    count += 1
                }
            }
        }
    }
    for(int i=0;i<10;i++) {
        for (j 0;j<1;j++){
            if (i != j){
                int candi = j*10000 + j * 1000+j*100+i*10+i;
                if(A <= candi and candi <= B) {
                    count += 1
                }
            }
        }
    }
    for(int i=0;i<10;i++) {
        for (int j=0;j<10;j++){
            for(int k=0; k<10;k++){
                if (i != j and k != j and k !=i){
                    int candi = j*10000 + k * 1000+j*100+k*10+i;
                    if(A <= candi and candi <= B) {
                        count += 1
                    }
                }
            }
        }
    }
    return 0;
}