#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> v;
    int N;
    cin >> N;

    int tip;
    for (int i = 0; i < N; i++)
    {
        cin >> tip;
        v.push_back(tip);
    }
    sort(v.begin(), v.end(), greater());

    long long ans = 0;
    for (int i = 0; i < N; i++)
        ans += max(0, v[i] - i);
    cout << ans << endl;
    return 0;
}