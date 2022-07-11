#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int a[20][26] = {0, }; // [손님][메뉴]
int n, m; // n : 손님 수, m : 메뉴 수

int menu[26] = {0, };

string s = "";
string res = "";

vector<string> ans; // answer

void Combination(int r){
  // m개 중 r개 뽑기
  vector<int> ind;
  for(int i=0; i<r; i++) ind.push_back(1);
  for(int i=0; i<m-r; i++) ind.push_back(0);

  sort(ind.begin(), ind.end());

  vector<pair<int, string> > v_tmp;

  do{
    string tmp = "";
    for(int i=0; i<ind.size(); i++){
      if(ind[i] == 1){
        tmp += s[i];
      }
    }
    // 작업 수행
    int cnt; int p=0;
    for(int i=0; i<n; i++){
      cnt = 0;
      for(int j=0; j<tmp.size(); j++){
        if(a[i][tmp[j]-'A']) cnt++;
      }
      if(cnt == tmp.size()) p++;
    }

    if(p >= 2){ // 2명 이상의 손님이 그 조합을 주문했어야 함
      if(v_tmp.size()==0) v_tmp.push_back(make_pair(p, tmp));
      else if(v_tmp.back().first > p) {} // 건너뛰기
      else{
        while(v_tmp.size() && v_tmp.back().first < p){
          v_tmp.pop_back();
        }
        v_tmp.push_back(make_pair(p, tmp));
      }
    }
    // 작업수행 끝
  }while(next_permutation(ind.begin(), ind.end()));

  // v_tmp에 있는 값들을 결과벡터에 넣어주기
  for(int i=0; i<v_tmp.size(); i++) ans.push_back(v_tmp[i].second);
}


vector<string> solution(vector<string> orders, vector<int> course) {

    for(int i=0; i<orders.size(); i++){
        for(int j=0; j<orders[i].size(); j++){
            a[i][orders[i][j]-'A'] = 1;
            menu[orders[i][j]-'A'] = 1;
        }
    }

    for(int i=0; i<26; i++){
        if(menu[i]){
            m++; // 메뉴 개수 카운트
            s += (i + 'A'); // 문자열에 메뉴 모으기
        }
    }

    n = orders.size(); // n : 손님 수

    for(int i=0; i<course.size(); i++){
        Combination(course[i]);
    }
    sort(ans.begin(), ans.end());
    return ans;
}