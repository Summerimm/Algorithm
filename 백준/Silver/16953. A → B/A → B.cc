#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int cnt = 1;
    while (true)
    {
        if (a == b)
        {
            cout << cnt << endl;
            return 0;
        }
        else if (a > b)
        {
            cout << -1 << endl;
            return 0;
        }

        if (b % 10 == 1)
            b = (b - 1) / 10;
        else if (b % 2 == 0)
            b /= 2;
        else
        {
            cout << -1 << endl;
            return 0;
        }
        cnt++;
    }
    return 0;
}