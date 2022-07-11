#include <string>
#include <vector>
#include <cctype>

using namespace std;

string step_1(string str){
    for(int i=0; i<str.size(); i++){
        str[i] = tolower(str[i]);
    }
    return str;
}

string step_2(string str){
    string res = "";
    for(int i=0; i<str.size(); i++){
        if(isalpha(str[i]) || isdigit(str[i]) || str[i]=='-' || str[i]=='.' || str[i]=='_') res += str[i];
    }
    return res;
}

string step_3(string str){
    string res = "";
    for(int i=0; i<str.size(); i++){
        if(!(str[i] == '.' && str[i+1] == '.')){
            res += str[i];
            continue;
        }

        // 연속으로 .이 2번이상 나온 경우
        while(str[i] == '.' && str[i+1] == '.'){
            if(i+1 < str.size()) i++;
        }
        if(str[i] == '.' && str[i-1] == '.'){
            res += '.';
        }
    } // for문 끝

    return res;
}

string step_4(string str){
    if(str[0] == '.'){
        str.erase(0, 1);
    }
    if(str[str.size()-1] == '.'){
        str.erase(str.size()-1, 1);
    }
    return str;
}

string step_5(string str){
    if(str.size()==0){
        string res = "a";
        return res;
    }
    return str;
}

string step_6(string str){
    if(str.size()>=16){
        string res = str.substr(0, 15);
        if(res[res.size()-1] == '.') res.erase(res.size()-1, 1);
        return res;
    }
    return str;
}

string step_7(string str){
    if(str.size() <= 2){
        string res = str;
        while(res.size() != 3){
            res += str[str.size()-1];
        }
        return res; // res의 길이가 3이되면 반환
    }
    return str;
}

string solution(string new_id) {
    return step_7(step_6(step_5(step_4(step_3(step_2(step_1(new_id)))))));
}