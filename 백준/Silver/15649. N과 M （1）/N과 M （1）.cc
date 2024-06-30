#include <iostream>
#include <vector>
#include <memory.h>
#define endl "\n"

using namespace std;

int n;
int r;
vector<int> v;
int visited[9];
void dfs(int a, int cnt)
{
    if (cnt == r)
    {
        for (auto i : v)
            cout << i << " ";
        cout << endl;
        return;
    }
    for (int i = 1; i <= n; i++)
    {
        if (visited[i] == 0)
        {
            visited[i] = 1;
            v.push_back(i);
            dfs(i, cnt + 1);
            v.pop_back();
            visited[i] = 0;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> r;
    for (int i = 1; i <= n; i++)
    {
        memset(visited, 0, sizeof(visited));
        visited[i] = 1;
        v.push_back(i);
        dfs(i, 1);
        v.pop_back();
        visited[i] = 0;
    }

    return 0;
}