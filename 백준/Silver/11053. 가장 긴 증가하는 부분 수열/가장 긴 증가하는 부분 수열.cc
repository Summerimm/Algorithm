#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int arr[1000];
int dp[1000];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int ans = 0;

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    for (int i = 0; i < N; ++i)
    {
        dp[i] = 1;
        for (int j = i - 1; j > -1; --j)
        {
            if (arr[i] > arr[j])
                dp[i] = max(dp[i], dp[j] + 1);
        }
        ans = max(ans, dp[i]);
    }

    cout << ans << endl;
    return 0;
}