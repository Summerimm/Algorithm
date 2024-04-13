#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int num[8];
int ans[8];
int N, M;

void dfs(int s, int depth)
{
    if (depth == M)
    {
        for (int i = 0; i < M; i++)
            cout << ans[i] << " ";
        cout << endl;
        return;
    }

    int last = 0;
    for (int i = s; i < N; i++)
    {
        if (last != num[i])
        {
            ans[depth] = num[i];
            last = num[i];
            dfs(i, depth + 1);
        }
    }
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        cin >> num[i];
    }

    sort(num, num + N);
    dfs(0, 0);

    return 0;
}