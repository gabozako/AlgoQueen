#include <bits/stdc++.h>
using namespace std;

// 방향 좌표 -> 동, 남, 서, 북 순서대로
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int n, m, s_x, s_y, dirty=0; // s_x, s_y: 시작점 좌표 // dirty: 더러운 칸의 개수

char room[21][21]; // 입력받는 배열
vector <pair<int, int> > dirty_v; // 더러운 칸 좌표 기록
int res = 1000000; // 결과 (최단거리)

int dp[21][21][(1<<10) + 1]; // 메모이제이션 배열

void input(){
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> room[i][j];

            if(room[i][j] == 'o'){ // 로봇청소기 시작 위치 기록
                s_x = i, s_y = j;
            }
            if(room[i][j] == '*'){
                dirty_v.push_back(make_pair(i, j)); // 더러운 칸 좌표 넣기
            }
        }
    }

    dirty = dirty_v.size(); // 더러운 칸의 개수
}

int dirty_idx(int x, int y){ // 쓰레기 좌표의 idx 반환
    int res;
    for(int i=0; i<dirty_v.size(); i++){
        if(dirty_v[i].first == x && dirty_v[i].second == y){
            res = i;
            break;
        }
    }
    return res;
}

void bfs(){
    queue <pair<pair<int, int>, pair<int, int> > > q;
    dp[s_x][s_y][0] = 0;
    q.push(make_pair(make_pair(s_x, s_y), make_pair(0, 0)));
    int x, y, ex, dis;

    while(!q.empty()){
        x = q.front().first.first; y = q.front().first.second;
        dis = q.front().second.first; ex = q.front().second.second; // 이동 횟수, 히스토리
        q.pop();

        if(ex == (1 << dirty)-1) break; // 쓰레기를 모두 청소한 경우

        for(int i=0; i<4; i++){
            int n_x = x + dx[i]; int n_y = y + dy[i];

            if(n_x >=0 && n_x < n && n_y >=0 && n_y < m){ // 다음으로 이동할 좌표가 범위 만족 시
                // 범위 만족 시
                if(room[n_x][n_y] == 'x') continue; // 가구인 경우 (이동 못함) -> continue
                else if(room[n_x][n_y] == 'o' || room[n_x][n_y] == '.'){
                    if(dis + 1 < dp[n_x][n_y][ex]){ // 갱신시켜야 하는 경우에 대해서만
                        dp[n_x][n_y][ex] = dis + 1; // 최소인 값으로 갱신
                        q.push(make_pair(make_pair(n_x, n_y), make_pair(dis+1, ex))); // 큐에 넣기
                    }
                }
                else if(room[n_x][n_y] == '*'){
                    // 쓰레기를 만난 경우
                    if(!(ex & (1<<dirty_idx(n_x, n_y)))){
                        // 방문한 적이 없는 경우
                        int next_dirty_status = ex | (1 << dirty_idx(n_x, n_y));
                        dp[n_x][n_y][next_dirty_status] = dis + 1;
                        q.push(make_pair(make_pair(n_x, n_y), make_pair(dis+1, next_dirty_status)));
                    }
                    else{
                        // 방문한 적이 있는 경우
                        if(dis + 1 < dp[n_x][n_y][ex]){ // 더 작은 값으로 갱신해야 하는 경우
                            dp[n_x][n_y][ex] = dis + 1; // 갱신하고
                            q.push(make_pair(make_pair(n_x, n_y), make_pair(dis+1, ex))); // 탐색 계속
                        }
                    }
                }
            }
        } // for문 끝
    } // while 문 끝 (bfs 끝)

    if(ex == (1 << dirty)-1) cout << dis << "\n"; // 쓰레기 다 치운 경우
    else cout << -1 << "\n"; // 쓰레기 다 못 치운 경우
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while(1){
        cin >> m >> n;
        if(m == 0 && n == 0) break;
        input();
        for(int i=0; i<21; i++){
            for(int j=0; j<21; j++){
                for(int k=0; k<(1<<11)+1; k++){
                    dp[i][j][k] = 9876321;
                }
            }
        }
        bfs();
    }

    return 0;
}