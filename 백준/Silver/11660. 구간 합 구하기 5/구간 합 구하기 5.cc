#include <iostream>

#define endl "\n"

using namespace std;

int N, M;
int arr[1025][1025];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 1; i < N + 1; i++)
    {
        for (int j = 1; j < N + 1; j++)
        {
            int a;
            cin >> a;
            if (i == 0 || j == 0)
            {
                arr[i][j] = 0;
            }
            if (i == 1 && j == 1)
            {
                arr[i][j] = a;
            }
            else if (i == 1)
            {
                arr[i][j] = arr[i][j - 1] + a;
            }
            else if (j == 1)
            {
                arr[i][j] = arr[i - 1][j] + a;
            }
            else
            {
                arr[i][j] = a + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1];
            }
        }
    }

    for (int i = 0; i < M; i++)
    {
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << arr[x2][y2] - arr[x2][y1 - 1] - arr[x1 - 1][y2] + arr[x1 - 1][y1 - 1] << endl;
    }
    return 0;
}
