#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> c) {
    sort(c.begin(), c.end(), greater<int>()); // 내림차순 정렬

    int ans = 0;

    for(int i=0; i<=c.size(); i++){ // max 값은 : c.size() -> 논문 수
        if(i+1 >= c[i]) return i;
    }

    return ans;
}