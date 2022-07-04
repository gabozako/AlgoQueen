#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N, r, c;
int sum[501], matrix[501][2], dp[501][501];

int main()
{
	cin >> N;

	for (int i=1; i<=N; i++){
        cin >> r >> c;
        matrix[i][0] = r;
        matrix[i][1] = c;
    }

	for (int i=1; i<N; i++){  // i: 구간범위의 크기 --> dp[x][x+2] 를 구하기
		for (int j=1; i+j<=N; j++){ // j: 구간범위의 시작점
			dp[j][i+j] = 1000000000;

			for (int k=j; k<=i+j; k++){ // k: 구간 범위를 두 부분으로 나눌 때의 기준점
				dp[j][i+j] = min(dp[j][i+j], dp[j][k]+dp[k + 1][i + j] + matrix[j][0]*matrix[k][1]*matrix[i+j][1]);
			}

		}
	}

	cout << dp[1][N];
    return 0;
}