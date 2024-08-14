#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

#define endl "\n"
#define INF pow(2, 63)

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, d;
    cin >> N >> d;

    long long ans = INF;

    vector<int> v;
    for (int i = 0; i < d; i++)
        v.push_back(i);

    do
    {
        int idx = 0;
        long long tmp = 0;
        // 0, 1, 2, 3, ... d-1까지 d!의 경우의 수에 대해서
        for (auto n : v)
        {
            // d진법으로 계산하기
            tmp += n * pow(d, idx);
            idx++;
        }
        // N보다 크고 ans보다 작으면? ans 업데이트.
        if (tmp > N && tmp < ans && v[v.size() - 1] != 0)
            ans = tmp;
    } while (next_permutation(v.begin(), v.end()));

    if (ans == INF)
        cout << -1 << endl;
    else
        cout << ans << endl;

    return 0;
}