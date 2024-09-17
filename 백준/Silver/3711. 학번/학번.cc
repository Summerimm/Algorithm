#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	vector<int> v1;
	set<int> s;

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		v1.clear();

		int N, num;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> num;
			v1.push_back(num);
		}

		int ans = 1;
		while (true) {
			s.clear();
			for (auto a : v1)
				s.insert(a % ans);

			if (s.size() == N) {
				cout << ans << endl;
				break;
			}
			ans++;
		}
	}

	return 0;
}