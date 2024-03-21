#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int dp[50001];

int main() {

	int n;

	cin >> n;

	for (int i = 1; i <= n; i++) {
		dp[i] = dp[i - 1] + 1;
		for (int j = 1; j*j <= i; j++) {
			dp[i] = min(dp[i], dp[i - j * j] + 1);
		}
	}

	cout << dp[n] << endl;

	return 0;
}