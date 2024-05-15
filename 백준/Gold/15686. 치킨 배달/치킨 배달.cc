#include <iostream>
#include <vector>
#include <algorithm>

#define INF int(1e9)
#define endl "\n"

using namespace std;
typedef pair<int, int> pii;

int N, M;
int dist[100][13];
pii ch[13];
pii user[100];
bool visited[13];
vector<int> selected;
int uidx, cidx;
int ans;

int calculate()
{
    int ret = 0;
    for (int i = 0; i < uidx; i++)
    {
        int tmp = INF;
        for (int j : selected)
            tmp = min(tmp, dist[i][j]);
        ret += tmp;
    }
    return ret;
}

void dfs(int idx, int cnt)
{
    if (cnt == M)
    {
        ans = min(ans, calculate());
        return;
    }
    for (int i = idx; i < cidx; i++)
    {
        if (visited[i] == true)
            continue;
        visited[i] = true;
        selected.push_back(i);
        dfs(i, cnt + 1);
        selected.pop_back();
        visited[i] = false;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int k;
    uidx = 0;
    cidx = 0;
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> k;
            if (k == 1)
                user[uidx++] = {i, j};
            else if (k == 2)
                ch[cidx++] = {i, j};
        }
    }

    for (int i = 0; i < uidx; i++)
        for (int j = 0; j < cidx; j++)
            dist[i][j] = abs(user[i].first - ch[j].first) + abs(user[i].second - ch[j].second);

    for (int i = 0; i < 13; i++)
        visited[i] = false;

    ans = INF;
    dfs(0, 0);
    cout << ans << endl;
    return 0;
}