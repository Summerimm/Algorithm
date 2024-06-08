#include <iostream>
#include <queue>
#include <memory.h>

#define endl "\n"

using namespace std;
typedef pair<int, int> pii;

int ans;
int N, M;
int board[101][101];
int boardCopy[100][100];
bool visited[101][101];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
queue<pii> q;

bool check()
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (board[i][j])
                return false;
    return true;
}

void melting()
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            boardCopy[i][j] = board[i][j];

    q = {};
    memset(visited, 0, sizeof(visited));

    ans++;

    q.push({0, 0});
    visited[0][0] = 1;

    while (!q.empty())
    {
        auto cur = q.front();
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = cur.first + dx[k];
            int ny = cur.second + dy[k];
            if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny])
                continue;
            if (board[nx][ny])
                board[nx][ny]++; // 치즈일 경우 공기를 만난 만큼 증가하게 됨
            if (board[nx][ny] == 0)
            {
                q.push({nx, ny});
                visited[nx][ny] = 1;
            }
        }
    }

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            if (board[i][j] - 1 >= 2)
                boardCopy[i][j] = 0;
            board[i][j] = boardCopy[i][j];
        }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> board[i][j];

    while (!check())
        melting();

    cout << ans << endl;

    return 0;
}