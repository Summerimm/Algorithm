#include <iostream>
#include <queue>

#define endl "\n"

using namespace std;

int n;
int cmd;
priority_queue<int, vector<int>, greater<int>> q;

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == 0){
			if (q.empty()) {
				cout << 0 << endl;
			}
			else {
				cout << q.top() << endl;
				q.pop();
			}
		}
		else {
			q.push(cmd);
		}
	}

	return 0;
}