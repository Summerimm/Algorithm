#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<int> failure(string pattern) {
	int M = pattern.length();
	vector<int> pi(M);

	pi[0] = 0;

	int j = 0;
	for (int i = 1; i < M; i++) {
		while (j > 0 && pattern[i] != pattern[j])
			j = pi[j - 1];
		if (pattern[i] == pattern[j])
			pi[i] = ++j;
	}
	return pi;
}


vector<int> KMP(string pattern, string text) {
	int M = pattern.length();
	int N = text.length();
	vector<int> pos;
	vector<int> pi = failure(pattern);

	int j = 0;
	for (int i = 0; i < N; i++) {
		while (j > 0 && text[i] != pattern[j])
			j = pi[j - 1];
		if (text[i] == pattern[j]) {
			if (j == M - 1) {
				pos.push_back(i - M + 1 + 1);
				j = pi[j];
			}
			else j++;
		}
	}
	return pos;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string text;
	getline(cin, text);
	string pattern;
	getline(cin, pattern);

	vector<int> answer = KMP(pattern, text);
	cout << answer.size() << "\n";
	for (int i = 0; i < answer.size(); ++i)
		cout << answer[i] << "\n";

	return 0;
}