#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int x1, y1, p1, q1, x2, y2, p2, q2;
	int x_left, x_right, y_left, y_right;
	int xdiff, ydiff;
	cin >> x1 >> y1 >> p1 >> q1;
	cin >> x2 >> y2 >> p2 >> q2;

	x_left = max(x1, x2);
	x_right = min(p1, p2);
	y_left = max(y1, y2);
	y_right = min(q1, q2);

	xdiff = x_right - x_left;
	ydiff = y_right - y_left;

	if (xdiff > 0 && ydiff > 0) cout << "FACE" << endl;
	else if (xdiff == 0 && ydiff == 0) cout << "POINT" << endl;
	else if (xdiff < 0 || ydiff < 0) cout << "NULL" << endl;
	else cout << "LINE" << endl;

	return 0;
}