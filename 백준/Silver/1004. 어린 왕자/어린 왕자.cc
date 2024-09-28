#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T, N;
    int sx, sy, ex, ey;
    int x, y, r;
    int a, b;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        a = 0, b = 0;
        cin >> sx >> sy >> ex >> ey;
        cin >> N;
        for (int i = 0; i < N; i++)
        {
            cin >> x >> y >> r;

            if ((x - sx) * (x - sx) + (y - sy) * (y - sy) <= r * r)
                if ((x - ex) * (x - ex) + (y - ey) * (y - ey) > r * r)
                    a++; // 이탈
            if ((x - ex) * (x - ex) + (y - ey) * (y - ey) <= r * r)
                if ((x - sx) * (x - sx) + (y - sy) * (y - sy) > r * r)
                    b++; // 진입
        }
        cout << a + b << endl;
    }
    return 0;
}