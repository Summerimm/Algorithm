#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    string str;
    vector<string> v;
    for (int t = 0; t < N; t++)
    {
        v.clear();
        for (int i = 0; i < 4; i++)
        {
            cin >> str;
            v.push_back(str);
        }
        sort(v.begin(), v.end());

        // 적힌 알파벳이 같으면서 숫자가 연속되는 세 장이 존재한다. 연속한 세 숫자는 서로 다른 숫자여야 한다.
        if (v[0][1] == v[1][1] && v[1][1] == v[2][1])
        {
            if ((int(v[0][0]) + 1 == int(v[1][0])) && (int(v[1][0]) + 1 == int(v[2][0])))
            {
                cout << ":)" << endl;
                continue;
            }
        }

        if (v[1][1] == v[2][1] && v[2][1] == v[3][1])
        {
            if ((int(v[1][0]) + 1 == int(v[2][0])) && (int(v[2][0]) + 1 == int(v[3][0])))
            {
                cout << ":)" << endl;
                continue;
            }
        }

        if (v[0][1] == v[2][1] && v[2][1] == v[3][1])
        {
            if ((int(v[0][0]) + 1 == int(v[2][0])) && (int(v[2][0]) + 1 == int(v[3][0])))
            {
                cout << ":)" << endl;
                continue;
            }
        }

        if (v[0][1] == v[1][1] && v[1][1] == v[3][1])
        {
            if ((int(v[0][0]) + 1 == int(v[1][0])) && (int(v[1][0]) + 1 == int(v[3][0])))
            {
                cout << ":)" << endl;
                continue;
            }
        }

        // 적힌 알파벳과 숫자가 모두 같은 세 장이 존재한다.
        if ((v[0] == v[1] && v[1] == v[2]) || (v[1] == v[2] && v[2] == v[3]))
        {
            cout << ":)" << endl;
            continue;
        }

        // 두 장씩 짝지었을 때, 짝을 지은 카드끼리 적힌 숫자와 알파벳이 같다.
        if (v[0] == v[1] && v[2] == v[3])
        {
            cout << ":)" << endl;
            continue;
        }
        else
            cout << ":(" << endl;
    }
    return 0;
}