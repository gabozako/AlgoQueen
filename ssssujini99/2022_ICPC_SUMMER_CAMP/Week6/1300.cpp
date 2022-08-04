#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <queue>
#include <unordered_map>
#include <cstring>
#include <sstream>
using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    ll n, k; cin >> n >> k; // 개수가 k개인거 찾기

    ll left = 1, right = n*n, res;

    while(left <= right){
        ll mid = (left + right) / 2;

        ll sum = 0;
        for(ll i=1; i<=n; i++){
            sum += min(n, (mid/i));
        }

        if(sum >= k){ // k개 이상인 것 중에 가장 작은 mid 찾기
            // cout << "mid: " << mid << endl;
            res = mid;
            right = mid - 1;
        }
        else left = mid + 1;
    }

    cout << res << endl;
    return 0;
}