#include <iostream>
#include <iomanip>
#include <math.h>

#define _USE_MATH_DEFINES
#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double R;
    cin >> R;
    cout << fixed << setprecision(6) << M_PI * R * R << endl;
    cout << 2 * R * R << endl;
    return 0;
}