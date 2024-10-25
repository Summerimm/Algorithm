#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int W, H, X, Y, P;
	int ans = 0;
	int x, y;
	cin >> W >> H >> X >> Y >> P;
	int R = H / 2;
	int rx1 = X, ry1 = Y + R, rx2 = X + W, ry2 = Y + R;
	for (int i = 0; i < P; i++) {
		cin >> x >> y;

		if (X <= x && x <= X + W && Y <= y && y <= Y + H) {
			ans++;
			continue;
		}
		else if (pow(x - rx1, 2) + pow(y - ry1, 2) <= R * R || pow(x - rx2, 2) + pow(y - ry2, 2) <= R * R)
			ans++;
	}

	cout << ans << endl;

	return 0;
}