#include <iostream>
#include <vector>

using namespace std;

double ccw(double x1, double y1, double x2, double y2, double x3, double y3) {
	double ret = x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1;
	return ret;
}

int main() {
    
	vector<pair<int, int>> v;
	int x, y;
	for (int i = 0; i < 3; i++) {
		cin >> x >> y;
		v.push_back({ x, y });
	}

	double ans = 0;
	ans = ccw(v[0].first, v[0].second, v[1].first, v[1].second, v[2].first, v[2].second);

	if (ans < 0) cout << -1;
	else if (ans == 0) cout << 0;
	else cout << 1;
	return 0;
}