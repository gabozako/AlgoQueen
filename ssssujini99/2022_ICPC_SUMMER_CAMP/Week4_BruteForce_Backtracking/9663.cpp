#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int row[16] = {0, };
int N, res = 0;

bool check(int idx, int val){ // row[idx] = val을 놓아도 되는지에 대한 확인여부
    for(int i=1; i<idx; i++){ // 이 전에 놓은 말들에 대해서 check 해주기
        if(row[i]==val || abs(val-row[i]) == idx-i) return false;
    }
    return true;
}

void NQueen(int cnt){
    if(cnt == N+1){
        res++;
    }
    else{
        for(int i=1; i<=N; i++){ // 말을 1부터 N에 놓을 수 있음
            if(check(cnt, i)){ // 유망하다면
                row[cnt] = i;
                NQueen(cnt+1); // 계속 다음 열로 나아가기
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    NQueen(1);
    cout << res << endl;
    return 0;
}