#include <iostream>

using namespace std;

int N;
char arr[3072][6143];
void draw(int row, int col) {
	arr[row][col] = '*';
	arr[row + 1][col - 1] = '*';
	arr[row + 1][col + 1] = '*';
	for (int i = -2; i < 3; i++)
		arr[row + 2][col + i] = '*';
}

void recursiveFuc(int len, int row, int col) {

	if (len == 3) {
		draw(row, col);
		return;
	}

	recursiveFuc(len / 2, row, col);
	recursiveFuc(len / 2, row + len / 2, col - len / 2);
	recursiveFuc(len / 2, row + len / 2, col + len / 2);
}

int main() {
	cin.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < 2 * N - 1; j++)
			arr[i][j] = ' ';

	recursiveFuc(N, 0, N - 1);		// 길이, 행, 열

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 2 * N - 1; j++)
			cout << arr[i][j];
		cout << '\n';
	}

	return 0;
}