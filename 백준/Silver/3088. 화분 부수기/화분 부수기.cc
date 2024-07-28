#include <iostream>
#define endl "\n"
using namespace std;

int N;
int g[1000001];
int ans;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int a, b, c;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> a >> b >> c;
        if (!(g[a] || g[b] || g[c]))
            ans++;
        g[a] = g[b] = g[c] = 1;
    }
    cout << ans << endl;
    return 0;
}