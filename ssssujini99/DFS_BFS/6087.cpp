#include <iostream>
#include <queue>
#include <vector>
using namespace std;


// 방향 좌표
int y_ar[4] = { 0,0,1,-1 };
int x_ar[4] = { 1,-1,0,0 };
char arr[100][100];

vector <pair<int, int> > v;
int visited[100][100] = { 0, };
int w, h;

int val, temp;

void bfs() {

	queue <pair<pair<int, int>, pair<int, int> > > q; //좌표, 거울 갯수, 방향
	q.push(make_pair(make_pair(v[0].first, v[0].second), make_pair(0, -1)));

	while (!q.empty()) {
		int y = q.front().first.first;
		int x = q.front().first.second;
		int mirror = q.front().second.first;
		int dir = q.front().second.second;
		q.pop();
		int temp;
		for (int i = 0; i < 4; i++) {
			int ny = y + y_ar[i];
			int nx = x + x_ar[i];
			if (ny < 0 || ny >= h || nx < 0 || nx >= w || arr[ny][nx] == '*' )
				continue;
			temp = mirror;
			if (dir != i)
				temp++;
			if (visited[ny][nx] >= temp) {
				visited[ny][nx] = temp;
				q.push(make_pair(make_pair(ny, nx), make_pair(temp, i)));
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);


	cin >> w >> h;
	for (int i = 0; i < h; i++) {
		cin >> arr[i];
		for (int j = 0; j < w; j++) {
			if (arr[i][j] == 'C')
				arr[i][j] = '.', v.push_back(make_pair(i, j));
			visited[i][j] = 1000000000;

		}
	}

	bfs();

	cout << visited[v[1].first][v[1].second] - 1 << endl;
	return 0;
}