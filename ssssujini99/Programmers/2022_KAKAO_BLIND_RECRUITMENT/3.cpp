#include <string>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <iostream>
#include <set>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> res; // 결과 벡터

    vector<int> v[1000]; // 한 차량의 입출차 내역 기록
    int parking_fees[1000] = {0, }; // 차량이 내야 할 금액
    set<string> s; //
    unordered_map<string, int> um; // 차량번호 - idx 매칭

    int ba_time = fees[0]; int ba_cost = fees[1];
    int per_time = fees[2]; int per_cost = fees[3];

    for(int i=0; i<records.size(); i++){
        string tmp = "";
        for(int j=6; j<10; j++) tmp += records[i][j];
        s.insert(tmp);
    }

    int idx = 0;

    for(auto i : s){
        um[i] = idx++;
    }

    for(int i=0; i<records.size(); i++){
        string tmp = "";
        for(int j=6; j<10; j++) tmp += records[i][j];
        int car_idx = um[tmp];

        int hour = (records[i][0] - '0')*10 + (records[i][1] - '0')*1;
        int minute = (records[i][3] - '0')*10 + (records[i][4] - '0')*1;
        int tot_min = hour*60 + minute;

        v[car_idx].push_back(tot_min);
    }


    for(int i=0; i<1000; i++){
        if(v[i].size() > 0){

            // 입차는 있는데 출차는 없는 경우의 예외처리
            if((v[i].size())%2){
                v[i].push_back(23*60+59); // 출차 -> 23:55분 넣어주기
            }

            int sum_time = 0;
            for(int j=0; j<v[i].size()-1; j=j+2){ // 누적 주차 시간 구하기
                sum_time += v[i][j+1] - v[i][j]; // 출차 시간 - 입차 시간
            }

            if(sum_time <= ba_time){
                parking_fees[i] = ba_cost;
            }
            else{
                int extra_cost = 0;
                if((sum_time - ba_time)%per_time) extra_cost = ((sum_time - ba_time)/(per_time) + 1)*(per_cost);
                else extra_cost = ((sum_time - ba_time)/(per_time))*(per_cost);

                parking_fees[i] = ba_cost + extra_cost;
            }

        }
    }

    for(int i=0; i<s.size(); i++){
        res.push_back(parking_fees[i]);
    }

    return res;
}