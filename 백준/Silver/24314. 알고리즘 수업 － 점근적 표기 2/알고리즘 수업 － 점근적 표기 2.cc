#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a1, a0;
    int c;
    int n0;
    cin >> a1 >> a0 >> c >> n0;

    if (c <= a1 && c * n0 <= a1 * n0 + a0)
        cout << 1;
    else
        cout << 0;
    return 0;
}