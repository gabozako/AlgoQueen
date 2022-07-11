#include <bits/stdc++.h>

using namespace std;

bool isPrime(long long num){
    if(num<2) return false;
    for(long long i=2; i<=sqrt(num); i++){
        if(num%i==0) return false;
    }
    return true;
}


int solution(int n, int k) {
    string s = ""; int result = 0;

    while(n){
        s += (n%k + '0');
        n = n/k;
    }
    reverse(s.begin(), s.end());

    string tmp = "";

    for(int i=0; i<s.size(); i++){
        while(s[i] != '0'){
            tmp += s[i++];
            if(i == s.size()) break;
        }

        if(s[i] == '0' && tmp.size()){
            long long nn = stoll(tmp);
            if(isPrime(nn)) result++;
            tmp = "";
        }
    }

    if(tmp.size()){ // 마지막 예외처리
        long long nn = stoll(tmp);
        if(isPrime(nn)) result++;
    }

    return result;

}