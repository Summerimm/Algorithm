#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>

#define endl "\n"

using namespace std;

int T;
int lcs[101][101][101];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
    
	string s1;
	string s2;
	string s3;

	cin >> s1;
	cin >> s2;
	cin >> s3;
	for (int i = 0; i < 101; i++)
		for (int j = 0; j < 101; j++)
			for (int k = 0; k < 101; k++)
				lcs[i][j][k] = 0;

	for (int i = 1; i <= (int)s3.length(); i++) {
		for (int j = 1; j <= (int)s2.length(); j++) {
			for (int k = 1; k <= (int)s1.length(); k++) {
				if (s3[i - 1] == s2[j - 1] && s3[i - 1] == s1[k - 1] && s2[j - 1] == s1[k - 1]) lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1;
				else lcs[i][j][k] = max(max(lcs[i - 1][j][k], lcs[i][j - 1][k]), lcs[i][j][k - 1]);
			}
		}
	}

	cout << lcs[(int)s3.length()][(int)s2.length()][(int)s1.length()] << endl;

	return 0;
}