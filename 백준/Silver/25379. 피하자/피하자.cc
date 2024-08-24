#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> even_idx;
    vector<int> odd_idx;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        if (num % 2 == 0)
            even_idx.push_back(i);
        else
            odd_idx.push_back(i);
    }

    // 홀수를 왼쪽으로 몰기
    long long move_odd_left = 0;
    for (int i = 0; i < odd_idx.size(); i++)
        move_odd_left += odd_idx[i] - i;

    // 짝수를 왼쪽으로 몰기
    long long move_even_left = 0;
    for (int i = 0; i < even_idx.size(); i++)
        move_even_left += even_idx[i] - i;

    long long ans = min(move_odd_left, move_even_left);

    cout << ans << endl;

    return 0;
}
