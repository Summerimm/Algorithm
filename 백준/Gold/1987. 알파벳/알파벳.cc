#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

int R, C;
char map[20][20];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int ans;
bool visited[26]; // 비트마스크를 사용하여 방문한 알파벳을 기록

void dfs(int x, int y, int cnt)
{
    ans = max(ans, cnt);

    for (int k = 0; k < 4; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx >= 0 && nx < R && ny >= 0 && ny < C)
        {
            char nextChar = map[nx][ny];
            int bit = nextChar - 'A';
            if (!visited[bit])
            {
                visited[bit] = true;
                dfs(nx, ny, cnt + 1);
                visited[bit] = false;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> R >> C;
    ans = 1;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            cin >> map[i][j];

    visited[map[0][0] - 'A'] = true;
    dfs(0, 0, 1);
    cout << ans << endl;
    return 0;
}
