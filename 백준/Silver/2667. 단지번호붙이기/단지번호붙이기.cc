#include <iostream>
#include <algorithm>
#include <queue>

#define endl "\n"

using namespace std;

int n;
int ans;
int cnt;
int idx;
char map[26][26];
bool visit[26][26];
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
queue<pair<int, int>> q;
int nx, ny, cx, cy;
int v[600];

void bfs(int x, int y) {
	cnt = 1;
	visit[x][y] = true;
	q.push({ x, y });
	while (!q.empty()) {
		cx = q.front().first;
		cy = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			nx = cx + dx[i];
			ny = cy + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < n && map[nx][ny] == '1' && !visit[nx][ny]) {
				q.push({ nx, ny });
				visit[nx][ny] = true;
				cnt++;
			}
		}
	}
	v[idx] = cnt;
	idx++;
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
			visit[i][j] = false;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == '1' && !visit[i][j]) {
				bfs(i, j);
				ans++;
			}
		}
	}

	cout << ans << endl;
	sort(v, v + idx);
	for (int i = 0; i < idx; i++) {
		cout << v[i] << endl;
	}

	return 0;
}