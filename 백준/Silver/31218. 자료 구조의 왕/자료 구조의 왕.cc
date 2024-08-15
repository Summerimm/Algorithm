#include <iostream>

#define endl "\n"
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int arr[1000][1000] = {
        0,
    };

    int N, M, Q;
    cin >> N >> M >> Q;

    int cnt = N * M;
    int cmd, dx, dy, r, c;
    for (int i = 0; i < Q; i++)
    {
        cin >> cmd;
        if (cmd == 3)
            cout << cnt << endl;
        else if (cmd == 2)
        {
            cin >> r >> c;
            cout << arr[r - 1][c - 1] << endl;
        }
        else
        {
            cin >> dx >> dy >> r >> c;
            int cx = r - 1;
            int cy = c - 1;
            while (arr[cx][cy] == 0)
            {
                arr[cx][cy] = 1;
                cnt--;
                cx += dx;
                cy += dy;
                if (cx < 0 || cx >= N || cy < 0 || cy >= M)
                    break;
            }
        }
    }
    return 0;
}