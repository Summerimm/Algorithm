#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

pair<int, int> calculate_strike_and_ball(int guess, int actual)
{
    int a1 = guess / 100, a2 = (guess / 10) % 10, a3 = guess % 10;
    int b1 = actual / 100, b2 = (actual / 10) % 10, b3 = actual % 10;

    int strike = 0, ball = 0;

    if (a1 == b1)
        strike++;
    if (a2 == b2)
        strike++;
    if (a3 == b3)
        strike++;

    if (a1 == b2 || a1 == b3)
        ball++;
    if (a2 == b1 || a2 == b3)
        ball++;
    if (a3 == b1 || a3 == b2)
        ball++;

    return {strike, ball};
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> candidates;

    for (int i = 1; i < 10; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            if (i == j)
                continue;
            for (int k = 1; k < 10; k++)
            {
                if (i == k || j == k)
                    continue;
                candidates.push_back(i * 100 + j * 10 + k);
            }
        }
    }

    int num, strike, ball;
    for (int t = 0; t < N; t++)
    {
        cin >> num >> strike >> ball;

        // 조건에 맞지 않는 후보들을 제거하는 과정
        vector<int> new_candidates;
        for (int candidate : candidates)
        {
            auto [s, b] = calculate_strike_and_ball(num, candidate);
            if (s == strike && b == ball)
                new_candidates.push_back(candidate); // 조건에 맞는 후보만 추가
        }
        candidates = new_candidates; // 조건에 맞는 후보들로 교체
    }

    cout << candidates.size() << endl;

    return 0;
}
