#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
	double xa, ya, xb, yb, xc, yc;
	double A, B, C;
	double c1, c2, c3;
	double mx, mn;

	cin >> xa >> ya >> xb >> yb >> xc >> yc;

	if ((xa == xb && xb == xc) || (ya == yb && yb == yc)) cout << -1.0 << endl;
	else if (xa - xb != 0 && xc - xb != 0 && (ya - yb) / (xa - xb) == (yc - yb) / (xc - xb)) cout << -1.0 << endl;
	else {
		fixed(cout);
		cout.precision(16);
		A = sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb));
		B = sqrt((xb - xc) * (xb - xc) + (yb - yc) * (yb - yc));
		C = sqrt((xc - xa) * (xc - xa) + (yc - ya) * (yc - ya));

		c1 = (A + B) * 2;
		c2 = (B + C) * 2;
		c3 = (C + A) * 2;
		mx = max(max(c1, c2), c3);
		mn = min(min(c1, c2), c3);
		cout << mx - mn << endl;
	}

	return 0;
}