#include <iostream>
#include <algorithm>
#include <vector>
#define endl "\n"

using namespace std;

int main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M, num;
	vector<int> A;
	vector<int> B;
	vector<int> ans;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> num;
		A.push_back(num);
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> num;
		B.push_back(num);
	}

	bool flag = true;
	int max_a, max_b, idx_a, idx_b;
	while (true) {
		while (true) {
			if (A.size() == 0 || B.size() == 0) {
				flag = false;
				break;
			}
			max_a = *max_element(A.begin(), A.end());
			idx_a = max_element(A.begin(), A.end()) - A.begin();
			max_b = *max_element(B.begin(), B.end());
			idx_b = max_element(B.begin(), B.end()) - B.begin();
			if (max_a == max_b) break;
			else if (max_a > max_b) A.erase(A.begin() + idx_a);
			else B.erase(B.begin() + idx_b);
		}
		if (!flag) break;

		ans.push_back(max_a);

		int tmp = 0;
		for (int i = idx_a + 1; i < A.size(); i++)
			A[tmp++] = A[i];
		for (int i = 0; i < idx_a + 1; i++)
			A.pop_back();

		tmp = 0;
		for (int i = idx_b + 1; i < B.size(); i++)
			B[tmp++] = B[i];
		for (int i = 0; i < idx_b + 1; i++)
			B.pop_back();
	}

	if (!ans.empty()) {
		cout << ans.size() << endl;
		for (auto a : ans) cout << a << " ";
	}
	else cout << 0;
	cout << endl;
	return 0;
}