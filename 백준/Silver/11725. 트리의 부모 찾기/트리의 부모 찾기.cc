#include <iostream>
#include <vector>

#define endl "\n"

using namespace std;

vector<int> v[100001];
bool visited[100001];
int parent[100001];

int N;

void dfs(int num)
{
    for (auto &e : v[num])
    {
        if (!visited[e])
        {
            visited[e] = true;
            parent[e] = num;
            dfs(e);
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N + 1; i++)
    {
        v[i].clear();
    }

    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    visited[1] = true;
    dfs(1);

    for (int i = 2; i < N + 1; i++)
    {
        cout << parent[i] << endl;
    }

    return 0;
}