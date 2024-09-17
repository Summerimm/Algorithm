#include <iostream>
#include <vector>

#define endl "\n"

using namespace std;

int N;
vector<int> v;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    v = vector<int>(N);
    for (int i = 0; i < N; i++)
        cin >> v[i];

    int ans = 0;
    int s = 0;
    int e = v.size();
    while (s < e)
    {
        int mx = 0;
        int idx = -1;
        for (int i = s; i < e; i++)
        {
            if (v[i] >= mx)
            {
                mx = v[i];
                idx = i;
            }
        }
        for (int i = s; i < idx; i++)
            ans += mx - v[i];
        s = idx + 1;
    }
    cout << ans << endl;
    return 0;
}