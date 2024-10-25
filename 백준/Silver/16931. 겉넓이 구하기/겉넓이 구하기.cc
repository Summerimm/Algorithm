#include <iostream>

using namespace std;

int main() {
	int arr[100][100];

	int N, M, num;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> num;
			arr[i][j] = num;
		}
	}

	int ans = 0;
	int prev;
	for (int i = 0; i < N; i++) {
		prev = 0;
		for (int j = 0; j < M; j++) {
			if (prev < arr[i][j])
				ans += arr[i][j] - prev;
			prev = arr[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		prev = 0;
		for (int j = M - 1; j >= 0; j--) {
			if (prev < arr[i][j])
				ans += arr[i][j] - prev;
			prev = arr[i][j];
		}
	}

	for (int j = 0; j < M; j++) {
		prev = 0;
		for (int i = 0; i < N; i++) {
			if (prev < arr[i][j])
				ans += arr[i][j] - prev;
			prev = arr[i][j];
		}
	}

	for (int j = 0; j < M; j++) {
		prev = 0;
		for (int i = N - 1; i >= 0; i--) {
			if (prev < arr[i][j])
				ans += arr[i][j] - prev;
			prev = arr[i][j];
		}
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (arr[i][j] > 0) ans += 2;

	cout << ans << endl;


	return 0;
}