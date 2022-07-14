#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> state; // idx에 따른 양, 늑대 정보 // 양: 0 // 늑대: 1
vector<int> v[20]; // 연결 정보를 담은 벡터
bool visited[20][20][20] = {0, }; // 노드번호, 양의 수, 늑대 수
int sheep = 0; int wolf = 0; // 총 양의 수, 총 늑대 수

int ans = 1;

void input(vector<vector<int>> edges){
    for(auto edge : edges){
        v[edge[0]].push_back(edge[1]);
        v[edge[1]].push_back(edge[0]);
    }
}

void dfs(int idx, int s, int w){
    if(idx==0){
        ans = max(ans, s);
    }

    for(int i=0; i<v[idx].size(); i++){
        int next_idx = v[idx][i];

        if(state[next_idx] == 0){
            // 다음으로 이동할 노드가 양인 경우
            if(visited[next_idx][s+1][w] == 0){ // 탐색하지 않았던 경우라면
                visited[next_idx][s+1][w] = 1;
                state[next_idx] = -1;
                dfs(next_idx, s+1, w);
                visited[next_idx][s+1][w] = 0;
                state[next_idx] = 0;
            }
        }
        else if(state[next_idx] == 1){
            // 다음으로 이동할 노드가 늑대인 경우
            if((s > w+1) && visited[next_idx][s][w+1] == 0){
                visited[next_idx][s][w+1] = 1;
                state[next_idx] = -1;
                dfs(next_idx, s, w+1);
                visited[next_idx][s][w+1] = 0;
                state[next_idx] = 1;
            }
        }
        else{ // 이미 방문한 노드인 경우
            if(visited[next_idx][s][w]==0){
                visited[next_idx][s][w] = 1;
                dfs(next_idx, s, w);
                visited[next_idx][s][w] = 0;
            }
        }
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    state = info;

    input(edges);
    state[0] = -1;
    dfs(0, 1, 0);

    return ans;
}