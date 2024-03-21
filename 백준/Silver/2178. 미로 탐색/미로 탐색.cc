#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

#define endl "\n"

using namespace std;

int n, m;
char map[101][101];
int check[101][101];
bool visit[101][101];
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };
int nx, ny, cx, cy;
pair<int, int> cur;
queue<pair<int, int>> q;

void bfs(int x, int y) {
	visit[x][y] = true;
	q.push({ x, y });

	while (!q.empty()) {
		cur = q.front();
		cx = cur.first;
		cy = cur.second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			nx = cx + dx[i];
			ny = cy + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visit[nx][ny] && map[nx][ny] == '1') {
				visit[nx][ny] = true;
				check[nx][ny] = check[cx][cy] + 1;
				q.push({ nx, ny });
			}
		}
	}
}


int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	for (int i = 0; i < 101; i++) {
		for (int j = 0; j < 101; j++) {
			map[j][j] = 0;
			check[i][j] = 1;
			visit[i][j] = false;
		}
	}

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}

	bfs(0, 0);
	cout << check[n - 1][m - 1] << endl;

	return 0;
}