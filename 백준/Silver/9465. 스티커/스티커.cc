#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

int T;
int N;
vector<int> v[2];

int main()
{
    cin >> T;
    for (int tc = 0; tc < T; tc++)
    {
        for (int i = 0; i < 2; i++)
        {
            v[i].clear();
        }

        cin >> N;
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < N + 1; j++)
            {
                if (j == 0)
                {
                    v[i].push_back(0);
                }
                else
                {
                    int a;
                    cin >> a;
                    v[i].push_back(a);
                }
            }
        }

        for (int j = 2; j < N + 1; j++)
        {
            for (int i = 0; i < 2; i++)
            {
                v[i][j] += max(v[abs(i - 1)][j - 1], v[abs(i - 1)][j - 2]);
            }
        }
        cout << max(v[0][N], v[1][N]) << endl;
    }

    return 0;
}