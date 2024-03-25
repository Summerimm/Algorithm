#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int get_distance(string a, string b) {
	int distance = 0;
	for (int i = 0; i < 4; i++) {
		if (a[i] != b[i]) { 
			distance += 1;
		}
	}
	return distance;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		vector<string> str;
		int N;
		cin >> N;
		for (int j = 0; j < N; j++) {
			string tmp;
			cin >> tmp;
			str.push_back(tmp);
		}
		if (N > 32) {
			cout << 0 << '\n';
		}
		else {
			int min_distance = 100;
			for (int i = 0; i < N - 2; i++) {
				for (int j = i + 1; j < N - 1; j++) {
					for (int k = j + 1; k < N; k++) {
						min_distance = min(min_distance, get_distance(str[i], str[j]) + get_distance(str[j], str[k]) + get_distance(str[i], str[k]));
					}
				}
			}
			cout << min_distance << '\n'; 
		}
	}

	return 0;
}