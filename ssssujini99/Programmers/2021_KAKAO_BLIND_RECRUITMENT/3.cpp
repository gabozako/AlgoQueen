#include <bits/stdc++.h>

using namespace std;

unordered_map<string, int> um_lang;
unordered_map<string, int> um_part;
unordered_map<string, int> um_car;
unordered_map<string, int> um_food;

void init(){
    um_lang.insert(make_pair("-", 9));
    um_lang.insert(make_pair("cpp", 1));
    um_lang.insert(make_pair("java", 2));
    um_lang.insert(make_pair("python", 3));

    um_part.insert(make_pair("-", 9));
    um_part.insert(make_pair("backend", 1));
    um_part.insert(make_pair("frontend", 2));

    um_car.insert(make_pair("-", 9));
    um_car.insert(make_pair("junior", 1));
    um_car.insert(make_pair("senior", 2));

    um_food.insert(make_pair("-", 9));
    um_food.insert(make_pair("chicken", 1));
    um_food.insert(make_pair("pizza", 2));
}

vector<int> solution(vector<string> info, vector<string> query) {
    init();

    vector<int> v[5000]; vector<int> ans;

    for(int i=0; i<info.size(); i++){
        stringstream ss(info[i]);
        string lang, part, car, food, score;
        ss >> lang >> part >> car >> food >> score;


        int num = um_lang[lang]*1000 + um_part[part]*100 + um_car[car]*10 + um_food[food]*1;

        v[num].push_back(stoi(score));
    }

    for(int i=0; i<query.size(); i++){
        stringstream ss(query[i]);
        string lang, part, car, a, food, score;
        ss >> lang >> a >> part >> a >> car >> a >> food >> score;


        int num = um_lang[lang]*1000 + um_part[part]*100 + um_car[car]*10 + um_food[food]*1;
        string s = to_string(num);

        if(s.find("9") != string::npos){
            // 시작
            vector<string> tmp_v;

            if(s[0] == '9'){
                tmp_v.push_back(to_string(1)+s.substr(1));
                tmp_v.push_back(to_string(2)+s.substr(1));
                tmp_v.push_back(to_string(3)+s.substr(1));
            }
            else{
                tmp_v.push_back(s);
            }

            if(s[1] == '9'){
                int t = tmp_v.size();
                for(int k=0; k<t; k++){
                    tmp_v.push_back(tmp_v[k].substr(0, 1)+to_string(1)+s.substr(2));
                    tmp_v.push_back(tmp_v[k].substr(0, 1)+to_string(2)+s.substr(2));
                }
                for(int k=0; k<t; k++) tmp_v.erase(tmp_v.begin());
            }

            if(s[2] == '9'){
                int t = tmp_v.size();
                for(int k=0; k<t; k++){
                    tmp_v.push_back(tmp_v[k].substr(0, 2)+to_string(1)+s.substr(3));
                    tmp_v.push_back(tmp_v[k].substr(0, 2)+to_string(2)+s.substr(3));
                }
                for(int k=0; k<t; k++) tmp_v.erase(tmp_v.begin());
            }

            if(s[3] == '9'){
                int t = tmp_v.size();
                for(int k=0; k<t; k++){
                    tmp_v.push_back(tmp_v[k].substr(0, 3)+to_string(1));
                    tmp_v.push_back(tmp_v[k].substr(0, 3)+to_string(2));
                }
                for(int k=0; k<t; k++) tmp_v.erase(tmp_v.begin());
            }

            int cnt = 0;

            for(int j=0; j<tmp_v.size(); j++){
                for(int k=0; k<v[stoi(tmp_v[j])].size(); k++){
                    if(v[stoi(tmp_v[j])][k] >= stoi(score)){
                        cnt++;
                    }
                }
            }
            ans.push_back(cnt);
            // 끝
        }
        else{
            int cnt = 0;
            for(int j=0; j<v[num].size(); j++){
                if(v[num][j] >= stoi(score)) cnt++;
            }
            ans.push_back(cnt);
        }

    }

    return ans;
}