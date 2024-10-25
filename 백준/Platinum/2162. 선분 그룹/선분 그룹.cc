#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Coor {
	int x, y;
};

vector<pair<Coor, Coor>> v;
int parent[3000];
int CCW(Coor A, Coor B, Coor C) {
	int ret = A.x * B.y + B.x * C.y + C.x * A.y - A.y * B.x - B.y * C.x - C.y * A.x;
	if (ret > 0) return 1;
	else if (!ret) return 0;
	else return -1;
}

bool isLined(Coor A, Coor B, Coor C) {
	if (A.x < B.x) return B.x < C.x;
	else if (B.x < A.x) return C.x < B.x;
	else
		if (A.y < B.y) return B.y < C.y;
		else if (B.y < A.y) return C.y < B.y;
}

int findParent(int x) {
	if (parent[x] == x) return x;
	return parent[x] = findParent(parent[x]);
}

void unionGroup(int a, int b) {
	a = findParent(a);
	b = findParent(b);
	if (a < b) parent[b] = a;
	else parent[a] = b;
}

int main() {

	int N;
	int x1, y1, x2, y2;
	cin >> N;

	for (int i = 0; i < N; i++)
		parent[i] = i;

	for (int i = 0; i < N; i++) {
		cin >> x1 >> y1 >> x2 >> y2;
		Coor A = { x1, y1 };
		Coor B = { x2, y2 };
		v.push_back({ A, B });
	}

	int res1, res2;
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			Coor A = v[i].first;
			Coor B = v[i].second;
			Coor C = v[j].first;
			Coor D = v[j].second;

			res1 = CCW(A, B, C) * CCW(A, B, D);
			res2 = CCW(C, D, A) * CCW(C, D, B);

			if (!res1 && !res2) {
				if ((isLined(A, B, C) && isLined(A, B, D)) || (isLined(B, A, C) && isLined(B, A, D))) continue;
				else
					if (findParent(i) != findParent(j)) unionGroup(i, j);
			}
			else if (res1 <= 0 && res2 <= 0)
				if (findParent(i) != findParent(j)) unionGroup(i, j);
		}
	}


	for (int i = 0; i < N; i++)
		parent[i] = findParent(parent[i]);

	unordered_map<int, int> um;
	for (int i = 0; i < N; i++) {
		if (!um.count(parent[i])) um[parent[i]] = 1;
		else um[parent[i]]++;
	}

	int mx = 0;
	for (auto a : um)
		if (mx < a.second) mx = a.second;

	cout << um.size() << endl;
	cout << mx << endl;


	return 0;
}