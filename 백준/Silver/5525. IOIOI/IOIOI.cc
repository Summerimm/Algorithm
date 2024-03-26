#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

#define endl "\n";

using namespace std;


int N, M;
int ans = 0;
string str;

int main() {
	cin >> N >> M >> str;

	for (int i = 0; i < M; i++) {
		int cnt = 0;
		if (str[i] == 'I') {
			while (str[i + 1] == 'O' && str[i + 2] == 'I') {
				cnt++;
				i += 2;
				if (cnt == N) {
					ans++;
					cnt--;
				}
			}
		}
	}
	cout << ans << endl;
	return 0;
}