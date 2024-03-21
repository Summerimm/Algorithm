#include <iostream>

#define endl "\n"

using namespace std;

long long dp[101];

int main() {
	int T;
	int n;
	cin >> T;

	fill(dp, dp + 101, 0);
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;

	for (int i = 6; i < 101; i++) {
		dp[i] = dp[i - 1] + dp[i - 5];
	}

	for (int i = 0; i < T; i++) {
		cin >> n;
		cout << dp[n] << endl;
	}

	return 0;
}