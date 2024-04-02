#include <iostream>
#include <string>
#include <algorithm>

#define endl "\n"

using namespace std;

int dp[1001][1001];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	string str1, str2;
	cin >> str1 >> str2;

	for (int i = 1; i < str2.length() + 1; i++) {
		for (int j = 1; j < str1.length() + 1; j++) {
			if (str2[i - 1] == str1[j - 1])
				dp[i][j] = dp[i-1][j-1] + 1;
			else dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
		}
	}
	cout << dp[str2.length()][str1.length()] << endl;
}