#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int M, N;
vector<int> v;
int ch[9] = {0, };

void Permutation(){
    if(v.size() == N){
        for(int i=0; i<v.size(); i++){
            cout << v[i] << " ";
        }
        cout << "\n";
    }
    else{
        for(int i=1; i<=M; i++){
            if(!ch[i]){
                ch[i] = 1;
                v.push_back(i);
                Permutation();

                ch[i] = 0;
                v.pop_back();
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> M >> N;

    Permutation();

    return 0;
}