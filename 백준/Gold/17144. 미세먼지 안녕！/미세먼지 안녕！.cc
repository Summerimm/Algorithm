#include <iostream>
#include <vector>

#define endl "\n"

using namespace std;
typedef pair<int, int> P;

int room[50][50];
int croom[50][50];
int pdir;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int main()
{
    int R, C, T;
    cin >> R >> C >> T;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
        {
            cin >> room[i][j];
            croom[i][j] = 0;
            if (room[i][j] == -1)
            {
                pdir = i;
            }
        }

    int cnt;
    while (T--)
    {
        // 미세먼지 확산
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                cnt = 0;
                if (room[i][j] == -1)
                    continue;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (nx >= 0 && nx < R && ny >= 0 && ny < C && room[nx][ny] != -1)
                    {
                        croom[i][j] += room[nx][ny] / 5;
                        cnt++;
                    }
                }
                if (room[i][j] != 0)
                {
                    croom[i][j] += max(0, room[i][j] - room[i][j] / 5 * cnt);
                }
            }
        }

        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                if ((i == pdir - 1 && j == 0) || (i == pdir && j == 0))
                    continue;
                room[i][j] = croom[i][j];
                croom[i][j] = 0;
            }
        }

        // 공기청정기
        for (int i = pdir - 3; i >= 0; i--) room[i + 1][0] = room[i][0];
        for (int i = 1; i <= C - 1; i++) room[0][i - 1] = room[0][i];
        for (int i = 1; i <= pdir - 1; i++) room[i - 1][C - 1] = room[i][C - 1];
        for (int i = C - 1; i > 1; i--) room[pdir - 1][i] = room[pdir - 1][i - 1];
        room[pdir - 1][1] = 0;

        for (int i = pdir + 2; i < R; i++) room[i - 1][0] = room[i][0];
        for (int i = 1; i < C; i++) room[R - 1][i - 1] = room[R - 1][i];
        for (int i = R - 2; i >= pdir; i--) room[i + 1][C - 1] = room[i][C - 1];
        for (int i = C - 2; i > 0; i--) room[pdir][i + 1] = room[pdir][i];
        room[pdir][1] = 0;
    }

    int ans = 2;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            ans += room[i][j];

    cout << ans << endl;

    return 0;
}