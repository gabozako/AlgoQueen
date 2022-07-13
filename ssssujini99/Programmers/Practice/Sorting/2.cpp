#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(const string &a, const string &b){
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    vector<string> v;

    for(int i=0; i<numbers.size(); i++){
        v.push_back(to_string(numbers[i]));
    }
    sort(v.begin(), v.end(), cmp);

    string s = "";
    for(int i=0; i<v.size(); i++) s += v[i];

    if(s[0]=='0') return "0";
    else return s;
}