#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
vector<int> v;
int ans[8];

void dfs(int s, int depth) {
	if (depth == M) {
		for (int i = 0; i < M; i++) cout << ans[i] << " ";
		cout << endl;
		return;
	}

	for (int i = s; i < N; i++) {
		ans[depth] = v[i];
		dfs(i, depth + 1);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	sort(v.begin(), v.end());
	dfs(0, 0);

	return 0;
}