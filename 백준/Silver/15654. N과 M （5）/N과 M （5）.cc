#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int M, N;
int num[8];
int tmp[8];
bool visited[8];

void comb(int idx, int depth, int v[8])
{
    if (depth == N)
    {
        for (int i = 0; i < N; i++)
        {
            cout << v[i] << " ";
        }
        cout << endl;
        return;
    }
    for (int i = 0; i < M; i++)
    {
        if (!visited[i])
        {
            v[depth] = num[i];
            visited[i] = true;
            comb(i, depth + 1, v);
            visited[i] = false;
        }
    }
}

int main()
{
    cin >> M >> N;
    for (int i = 0; i < M; i++)
    {
        int a;
        cin >> a;
        num[i] = a;
    }

    sort(num, num + M);

    for (int i = 0; i < M; i++)
    {
        visited[i] = true;
        fill(tmp, tmp + 8, 0);
        tmp[0] = num[i];
        comb(i, 1, tmp);
        visited[i] = false;
    }

    return 0;
}