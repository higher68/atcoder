#include<bits/stdc++.h>
using namespace std;
int main(void) {
    int A, B; cin >>A >> B;
    int count = 0;
    //cout << "XXXXX" << endl;
    for(int i=1;i<10;i++) {
        int candi=i*10000 + i * 1000+i*100+i*10+i;
        //cout << candi << endl;
        if(A <= candi and candi <= B) {
            //cout << candi << "dayo" << endl;
            count += 1;
        }
    }
    //cout << "XXYXX" << endl;
    for(int i=1;i<10;i++) {
        for (int j=0;j<10;j++){
            if (i != j){
                int candi = i*10000 + i * 1000+j*100+i*10+i;
                //cout << candi << endl;
                if(A <= candi and candi <= B) {
                    //cout << candi << "dayo" << endl;
                    count += 1;
                }
            }
        }
    }
    //cout << "XYYYX" << endl;
    for(int i=1;i<10;i++) {
        for (int j=0;j<10;j++){
            if (i != j){
                int candi = i*10000 + j * 1000+j*100+j*10+i;
                //cout << candi << endl;
                if(A <= candi and candi <= B) {
                    //cout << candi << "dayo" << endl;
                    count += 1;
                }
            }
        }
    }
    //cout << "XZYZX" << endl;
    for(int i=1;i<10;i++) {
        for (int j=0;j<10;j++){
            for(int k=0; k<10;k++){
                if (i != j and k != j and k !=i){
                    int candi = i*10000 + k * 1000+j*100+k*10+i;
                    //cout << candi << endl;
                    if(A <= candi and candi <= B) {
                        //cout << candi << "dayo" << endl;
                        count += 1;
                    }
                }
            }
        }
    }
    //cout << "XYXYX" << endl;
    for(int i=1;i<10;i++) {
        for (int j=0;j<10;j++){
            if (i != j){
                int candi = i*10000 + j * 1000+i*100+j*10+i;
                //cout << candi << endl;
                if(A <= candi and candi <= B) {
                    //cout << candi << "dayo" << endl;
                    count += 1;
                }
            }
        }
    }
    cout << count << endl;
    return 0;
}