#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    int ta = 1, tb = 1, tc = 1;
    int ret = 1;
    while (!(ta == a && tb == b && tc == c))
    {
        ta++;
        tb++;
        tc++;
        if (ta == 16)
            ta = 1;
        if (tb == 29)
            tb = 1;
        if (tc == 20)
            tc = 1;
        ret++;
    }
    cout << ret << endl;
    return 0;
}