#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

struct Coor {
	long long x, y;
};

bool isLined(Coor A, Coor B, Coor C) {
	if (A.x < B.x) return B.x < C.x;
	else if (B.x < A.x) return C.x < B.x;
	else
		if (A.y < B.y) return B.y < C.y;
		else if (B.y < A.y) return C.y < B.y;
}

int CCW(Coor A, Coor B, Coor C) {
	long long ret = A.x * B.y + B.x * C.y + C.x * A.y;
	ret -= A.x * C.y + B.x * A.y + C.x * B.y;
	if (ret > 0) return 1;
	else if (!ret) return 0;
	else return -1;
}

int main() {
	long long x1, y1, x2, y2, x3, y3, x4, y4;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
	Coor A = { x1, y1 };
	Coor B = { x2, y2 };
	Coor C = { x3, y3 };
	Coor D = { x4, y4 };

	int ans1 = CCW(A, B, C) * CCW(A, B, D);
	int ans2 = CCW(C, D, A) * CCW(C, D, B);

	if (!ans1 && !ans2) {
		if ((isLined(A, B, C) && isLined(A, B, D)) || (isLined(B, A, C) && isLined(B, A, D))) cout << 0 << endl;
		else cout << 1 << endl;
	}
	else if (ans1 <= 0 && ans2 <= 0) cout << 1 << endl;
	else cout << 0 << endl;

	return 0;
}