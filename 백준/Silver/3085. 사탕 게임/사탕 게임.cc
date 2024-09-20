#include <iostream>

#define endl "\n"

using namespace std;

int N;
char arr[51][51];
string str;
int ans = 0;

int Count(int type, int x)
{
    int anstmp = 0;
    int tmp = 1;

    char curr;
    char prev;
    if (type == 0)
        prev = arr[x][0];
    else
        prev = arr[0][x];

    for (int i = 1; i < N; i++)
    {
        if (type == 0)
            curr = arr[x][i];
        else
            curr = arr[i][x];

        if (curr == prev)
            tmp++;
        else
        {
            anstmp = max(anstmp, tmp);
            prev = curr;
            tmp = 1;
        }
    }
    anstmp = max(anstmp, tmp);
    return anstmp;
}

void RightSwap(int r, int c)
{
    swap(arr[r][c], arr[r][c + 1]);
    ans = max(ans, Count(0, r));
    ans = max(ans, Count(1, c));
    ans = max(ans, Count(1, c + 1));
    swap(arr[r][c], arr[r][c + 1]);
}

void DownSwap(int r, int c)
{
    swap(arr[r][c], arr[r + 1][c]);
    ans = max(ans, Count(0, r));
    ans = max(ans, Count(0, r + 1));
    ans = max(ans, Count(1, c));
    swap(arr[r][c], arr[r + 1][c]);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> str;
        for (int j = 0; j < N; j++)
            arr[i][j] = str[j];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (j < N - 1)
                RightSwap(i, j);
            if (i < N - 1)
                DownSwap(i, j);
        }
    }

    cout << ans << endl;
    return 0;
}