#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef pair<int, int> pii;

struct cmp {
	bool operator()(pii A, pii B) {
		return A.first != B.first ? A.first < B.first : A.second < B.second;
	}
};

int calculate(int x1, int y1, int x2, int y2) {
	return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}

int main() {
	int T;
	int x, y;
	int diag1, diag2;
	int A, B, C, D;
	vector<pii> v;
	cin >> T;
	for (int t = 0; t < T; t++) {
		v.clear();
		for (int i = 0; i < 4; i++) {
			cin >> x >> y;
			v.push_back(make_pair(x, y));
		}
		sort(v.begin(), v.end(), cmp());

		A = calculate(v[0].first, v[0].second, v[1].first, v[1].second);
		B = calculate(v[1].first, v[1].second, v[3].first, v[3].second);
		C = calculate(v[2].first, v[2].second, v[0].first, v[0].second);
		D = calculate(v[3].first, v[3].second, v[2].first, v[2].second);
		diag1 = calculate(v[0].first, v[0].second, v[3].first, v[3].second);
		diag2 = calculate(v[1].first, v[1].second, v[2].first, v[2].second);
		if (A == B && B == C && C == D && D == A && diag1 == diag2)
			cout << 1 << endl;
		else
			cout << 0 << endl;
	}
	return 0;
}