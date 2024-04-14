#include <iostream>
#include <memory.h>
#define endl "\n"

using namespace std;

int N, M;
int num[8];
int ans[8];

void dfs(int start, int depth)
{
    if (depth == M)
    {
        for (int i = 0; i < M; i++)
            cout << ans[i] << " ";
        cout << endl;
        return;
    }

    for (int i = start; i < N; i++)
    {
        ans[depth] = num[i];
        dfs(i, depth + 1);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    memset(num, 0, sizeof(num));
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        num[i] = i + 1;
    }

    dfs(0, 0);

    return 0;
}