#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int a[9][9] = {0, };
vector<pair<int, int> > v;
int cnt_zero = 0;

bool Check(int x, int y, int val){
    // a[x][y] = val 에 대한 가능성 여부 확인
    // 가로, 세로, 3*3 정사각형 확인

    for(int i=0; i<9; i++){
        if(i!=y && a[x][i] == val) return false;
        if(i!=x && a[i][y] == val) return false;
    }

    int s_x = x; int s_y = y;
    if(x%3 == 1) s_x -= 1;
    else if(x%3 == 2) s_x -= 2;
    else {}

    if(y%3 == 1) s_y -= 1;
    else if(y%3 == 2) s_y -= 2;
    else {}

    for(int i=s_x; i<s_x+3; i++){
        for(int j=s_y; j<s_y+3; j++){
            if(i!=x && j!=y && a[i][j]==val) return false;
        }
    }

    return true;
}

void Sudoku(int count){
    if(count == v.size()){
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                cout << a[i][j] << " ";
            }
            cout << "\n";
        }
        exit(0);
    }

    for(int i=1; i<=9; i++){
        int x = v[count].first; int y = v[count].second;
        if(Check(x, y, i)){
            a[x][y] = i;
            Sudoku(count+1);
            a[x][y] = 0;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cin >> a[i][j];
            if(a[i][j] == 0) v.push_back(make_pair(i, j));
        }
    }

    Sudoku(0);
    return 0;
}