#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int arr[1001][1001];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    arr[1][1] = 1;
    int mx = 1;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if (i == 1 && j == 1)
                continue;
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]) + 1;
            mx = max(mx, arr[i][j]);
        }
    }

    if (mx > K)
        cout << "NO" << endl;
    else
    {
        cout << "YES" << endl;
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= M; j++)
                cout << arr[i][j] << " ";
            cout << endl;
        }
    }
    return 0;
}