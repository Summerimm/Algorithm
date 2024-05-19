#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int a, b;
        cin >> a >> b;

        int ans = 1;
        int r = 1;
        for (int i = b; i > b - a; i--)
        {
            ans *= i;
            ans /= r;
            r++;
        }
        cout << ans << endl;
    }
    return 0;
}