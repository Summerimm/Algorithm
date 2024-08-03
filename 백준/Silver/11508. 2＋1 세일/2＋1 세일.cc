#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, num;
    vector<int> v;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v.push_back(num);
    }
    sort(v.begin(), v.end(), greater());

    int ans = 0;
    for (int i = 0; i < N; i++)
    {
        if (i % 3 == 2)
            continue;
        ans += v[i];
    }
    cout << ans << endl;
    return 0;
}