#include <iostream>
#include <memory.h>

#define endl "\n"

using namespace std;

int num[100001];

struct SegTree {
	int base;
	long long tree[1 << 18];

	SegTree() {};

	int setup(int n) {
		base = 1;
		while (base < n) base <<= 1;

		memset(tree, 0, sizeof(tree));
		base--;
		return base;
	}

	void update(int i, int k) {
		i += base;
		tree[i] += k;
		for (i >>= 1; i; i >>= 1) {
			tree[i] = tree[i << 1] + tree[i << 1 | 1];
		}
	}

	long long sum(int id, int left, int right, int start, int end) {
		if (right < start || left > end) return 0;
		if (start >= left && end <= right) return tree[id];

		int mid = (start + end) / 2;
		long long left_sum = sum(id << 1, left, right, start, mid);
		long long right_sum = sum(id << 1 | 1, left, right, mid + 1, end);
		return left_sum + right_sum;
	}
};

int N;
int q;
int cmd;
int target;
SegTree T;
int main() {
	
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	int b = T.setup(N + 1);
	for (int i = 0; i < N; i++) cin >> num[i];

	cin >> q;
	for (int i = 0; i < q; i++) {
		cin >> cmd;
		if (cmd == 1) {
			int s, e, amount;
			cin >> s >> e >> amount;
			T.update(s, amount);
			T.update(e + 1, -amount);
		}
		else {
			cin >> target;
			long long ans = T.sum(1, 1, target, 1, b + 1);
			cout << num[target - 1] + ans << endl;
		}
	}

	return 0;
}