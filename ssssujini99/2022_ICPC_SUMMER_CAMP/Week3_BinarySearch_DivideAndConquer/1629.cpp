#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

long long a, b, c;

long long func(long long A, long long B){
    if(B == 0) return 1;
    if(B == 1) return A%c;

    long long half = func(A, B/2) % c;

    half = (half * half)%c;
    if(B%2) half = ((half%c) * (A%c));
    return half % c;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> a >> b >> c;

    cout << func(a, b) << endl;
    return 0;
}