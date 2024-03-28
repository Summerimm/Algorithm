#include <iostream>
#include <set>

#define endl "\n"

using namespace std;

int n, m;

void comb(int num, int depth, set<int> s) {

	if (depth == m) {
		for (auto& e : s) {
			cout << e << " ";
		}
		cout << endl;
		return;
	}
	for (int i = num + 1; i <= n; i++) {
		s.emplace(i);
		comb(i, depth + 1, s);
		s.erase(i);
	}
}

int main() {
	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		comb(i, 1, { i });
	}

	return 0;
}