#include <bits/stdc++.h>
using namespace std;

int cal_time(string s){
    int time = (s[0]-'0')*10 + (s[1]-'0')*1;
    int min = (s[3]-'0')*10 + (s[4]-'0')*1;
    int tot_time = time*60 + min;
    return tot_time;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> v[10000];
    vector<int> res;

    for(auto& record : records){
        stringstream ss(record);
        string a, b, c;
        ss >> a >> b >> c;

        v[stoi(b)].push_back(cal_time(a));
    }


    for(int i=0; i<10000; i++){
        if(v[i].size()){
            if(v[i].size()%2) v[i].push_back(23*60+59);

            int tot_time = 0;
            for(int j=0; j<v[i].size()-1; j+=2){
                tot_time += v[i][j+1] - v[i][j];
            }

            int tot_fees = fees[1];

            if(tot_time > fees[0]){ // 누적시간 > 기본시간인 경우
                int extra_fees = 0;
                if((tot_time - fees[0])%fees[2]){
                    extra_fees = ((tot_time - fees[0])/fees[2] + 1)*fees[3];
                }
                else extra_fees = ((tot_time - fees[0])/fees[2])*fees[3];

                tot_fees += extra_fees;
            }

            res.push_back(tot_fees);
        }
    }

    return res;
}