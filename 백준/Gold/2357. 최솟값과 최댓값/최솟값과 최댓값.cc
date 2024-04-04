#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;
typedef pair<int, int> pii;

struct SegTree {
	int base;
	pii tree[1 << 18];

	SegTree() {}

	void init(int n, int arr[]) {
		base = 1;
		while (base < n) base <<= 1;

		for (int i = n; i < base; ++i) tree[base + i] = { 1, 1000000000 };
		base--;
		for (int i = 1; i <= n; ++i) tree[base + i] = { arr[i - 1], arr[i - 1] };
		for (int i = base; i >= 1; --i) {
			tree[i].first = max(tree[i << 1].first, tree[i << 1 | 1].first);
			tree[i].second = min(tree[i << 1].second, tree[i << 1 | 1].second);
		}
	}

	pii findMinMax(int id, int left, int right, int start, int end) {
		if (left > end || right < start) return { 1, 1000000000 };
		if (left <= start && right >= end) return tree[id];

		int mid = (start + end) / 2;
		pii left_minmax = findMinMax(id << 1, left, right, start, mid);
		pii right_minmax = findMinMax(id << 1 | 1, left, right, mid + 1, end);

		return { max(left_minmax.first, right_minmax.first), min(left_minmax.second, right_minmax.second) };
	}
};


SegTree T;
int b;
int arr[100000];

int main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    
	int N, M;
	cin >> N >> M;

	b = 1;
	while (b < N) b <<= 1;

	int a;
	for (int i = 0; i < N; i++) {
		cin >> a;
		arr[i] = a;
	}

	T.init(N, arr);

	int left, right;
	for (int i = 0; i < M; i++) {
		cin >> left >> right;
		pii P = T.findMinMax(1, left, right, 1, b);
		cout << P.second << " " << P.first << endl;
	}
    
	return 0;
}