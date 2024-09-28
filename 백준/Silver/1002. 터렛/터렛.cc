#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T, x1, y1, r1, x2, y2, r2;
    int d;
    int left, right;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

        d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        left = (r1 - r2) * (r1 - r2);
        right = (r1 + r2) * (r1 + r2);

        if (d == 0)
        {
            // 완전히 일치할 경우 -> -1
            if (left == 0)
                cout << -1 << endl;
            else
                cout << 0 << endl;
        }
        // 한 점에서 만날 경우(외접 / 내접)
        else if (d == left || d == right)
            cout << 1 << endl;
        // 두 점에서 만날 경우
        else if (d > left && d < right)
            cout << 2 << endl;
        else
            cout << 0 << endl;
    }
    return 0;
}