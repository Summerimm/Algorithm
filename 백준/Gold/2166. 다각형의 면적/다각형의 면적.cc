#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

double ccw(double x1, double y1, double x2, double y2, double x3, double y3) {
	double ret = x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1;
	ret /= 2;
	return ret;
}

int main() {
	vector<pair<int, int>> v;
	int x, y;
	int N;
    
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> x >> y;
		v.push_back({ x, y });
	}

	double ans = 0;
	for (int i = 1; i < N; i++)
		ans += ccw(v[0].first, v[0].second, v[i - 1].first, v[i - 1].second, v[i].first, v[i].second);

	fixed(cout);
	cout.precision(1);
	cout << abs(ans) << endl;
	return 0;
}