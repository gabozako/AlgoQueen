#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <iostream>

using namespace std;


vector<int> solution(vector<string> id_list, vector<string> report, int k) {

    int user_cnt[1000] = {0, }; // 각 유저별로 신고당한 횟수
    int a[1000][1000] = {0, }; // 각 유저별 신고한 유저 매칭 배열
    vector<int> k_user_idx; // k번 이상 신고당한 유저의 idx를 담는 벡터
    vector<int> res; // 결과를 담는 벡터

    unordered_map<string, int> um;

    for(int i=0; i<id_list.size(); i++){
        um[id_list[i]] = i; // 유저 마다 idx 매겨주기
    }

    for(int i=0; i<report.size(); i++){
        string s1 = ""; string s2 = "";
        int j=0;
        for(j=0; j<report[i].size(); j++){
            if(report[i][j] == ' ') break;
            s1 += report[i][j];
        }
        j++;
        for(; j<report[i].size(); j++){
            s2 += report[i][j];
        }

        // s1 --(신고)--> s2

        if(a[um[s1]][um[s2]] == 0) user_cnt[um[s2]]++; // 신고당한 횟수 카운트
        a[um[s1]][um[s2]] = 1; // s1 --(신고)--> s2 를 기록

    }

    for(int i=0; i<id_list.size(); i++){
        if(user_cnt[i] >= k) k_user_idx.push_back(i);
    }

    for(int i=0; i<id_list.size(); i++){
        int t = 0;
        for(int j=0; j<k_user_idx.size(); j++){
            if(a[i][k_user_idx[j]] == 1) t++;
        }
        res.push_back(t);
    }

    return res;
}