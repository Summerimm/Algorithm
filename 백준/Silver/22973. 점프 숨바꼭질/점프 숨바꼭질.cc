#include <iostream>


#define endl "\n"

using namespace std;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long K;
    cin >> K;

    int cnt = 0;
    long long jump = 1;

    K = abs(K);
    if (K == 0)
    {
        cout << 0 << endl;
        return 0;
    }

    if (K % 2 == 0)
    {
        cout << -1 << endl;
        return 0;
    }

    while (K > 0)
    {
        jump *= (jump * 2) - 1;
        K /= 2;
        cnt++;
    }
    cout << cnt << endl;
    return 0;
}