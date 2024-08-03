#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef pair<int, int> pii;

int N, M;
char arr[2500][2500];
vector<pii> v;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == '1')
				v.push_back({ i, j });
		}
	}

	bool flag = false;
	for (pii p : v) {
		flag = true;
		int r = p.first;
		int c = p.second;

		int x1 = r;
		int x2 = r;
		int y1 = c;
		int y2 = c;

		for (int i = 1; i < 10; i++) {
			int cnt = 0;
			x1 += 1;
			x2 -= 1;
			y1 += 1;
			y2 -= 1;
			for (int j = y2; j <= y1; j++) {
				if (j >= 0 && j < M && x1 >= 0 && x1 < N && arr[x1][j] == '1')
					cnt++;
				if (j >= 0 && j < M && x1 >= 0 && x2 < N && arr[x2][j] == '1')
					cnt++;
			}

			for (int j = x2 + 1; j < x1; j++) {
				if (j >= 0 && j < N && y1 >= 0 && y1 < M && arr[j][y1] == '1')
					cnt++;
				if (j >= 0 && j < N && y2 >= 0 && y2 < M && arr[j][y2] == '1')
					cnt++;
			}

			if (cnt != 1) {
				flag = false;
				break;
			}
		}

		if (flag) {
			cout << r << " " << c << endl;
			break;
		}
	}

	if (!flag) {
		cout << -1 << endl;
	}

	return 0;
}