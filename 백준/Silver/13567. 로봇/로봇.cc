#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    pair<int, int> dir[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    string cmd;
    int M, N, d;
    int r = 0, c = 0, k = 0;
    bool flag = true;

    cin >> M >> N;
    while (N--)
    {
        cin >> cmd >> d;
        if (cmd == "MOVE")
        {
            r += dir[k].first * d;
            c += dir[k].second * d;
        }
        else
        {
            if (d == 0)
                k = (k + 1) % 4;
            else
                k = (k - 1 + 4) % 4;
        }
        if (r >= M || c >= M || r < 0 || c < 0)
        {
            flag = false;
            break;
        }
    }

    if (flag)
        cout << c << " " << r << endl;
    else
        cout << -1 << endl;
    return 0;
}
