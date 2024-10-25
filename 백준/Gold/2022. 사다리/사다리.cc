#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

double x, y, c;
double func(double mid) {
	double a = sqrt(x * x - mid * mid);
	double b = sqrt(y * y - mid * mid);
	return a * b / (a + b);
}

int main() {
	cin >> x >> y >> c;

	double low = 0;
	double high = min(x, y);
	double mid = 0;
	double res = 0;

	while (high - low > 0.0001) {
		mid = (low + high) / 2;
		if (func(mid) >= c) {
			low = mid;
			res = mid;
		}
		else
			high = mid;
	}

	fixed(cout);
	cout.precision(3);
	cout << res << endl;

	return 0;
}