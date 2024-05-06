#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    int x;
    int ret = 0;
    cin >> x;
    while (x != 0)
    {
        ret += x % 2;
        x /= 2;
    }
    cout << ret << endl;
    return 0;
}