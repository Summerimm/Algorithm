#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int n;
int stair[301];
int dp[301];

int main() {
	
	int score;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> score;
		stair[i + 1] = score;
	}

	dp[1] = stair[1];
	dp[2] = stair[2] + stair[1];
	dp[3] = max(stair[3] + stair[1], stair[2] + stair[3]);

	for (int i = 4; i < n + 1; i++) {
		dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i]);
	}

	cout << dp[n] << endl;
	return 0;
}