#include <iostream>
#include <algorithm>
#include <math.h>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    int arr[9][9];
    string str;

    cin >> N >> M;
    cin.ignore();
    for (int i = 0; i < N; i++)
    {
        getline(cin, str);
        for (int j = 0; j < M; j++)
            arr[i][j] = str[j] - '0';
    }

    // 행, 열 각각 공차는 0부터 N-1, M-1까지
    // 행, 열 둘 다 0인 경우 제외(0, 증가, 감소)

    int r, c, tmp, sqrttmp;
    int ans = -1;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        { // 모든 좌표에 대해서 시작
            for (int k = 0; k < N; k++)
            {
                for (int l = 0; l < M; l++)
                { // 행, 열에 대한 증감분
                    if (k == 0 && l == 0)
                    {
                        tmp = arr[i][j];
                        sqrttmp = static_cast<int>(sqrt(tmp));
                        if (sqrttmp * sqrttmp == tmp)
                            ans = max(tmp, ans);
                        continue;
                    }

                    tmp = 0;
                    r = i, c = j;
                    while (r < N && c < M && r >= 0 && c >= 0)
                    {
                        tmp *= 10;
                        tmp += arr[r][c];
                        r += k;
                        c += l;
                        sqrttmp = static_cast<int>(sqrt(tmp));
                        if (sqrttmp * sqrttmp == tmp)
                            ans = max(tmp, ans);
                    }

                    tmp = 0;
                    r = i, c = j;
                    while (r < N && c < M && r >= 0 && c >= 0)
                    {
                        tmp *= 10;
                        tmp += arr[r][c];
                        r += k;
                        c -= l;
                        sqrttmp = static_cast<int>(sqrt(tmp));
                        if (sqrttmp * sqrttmp == tmp)
                            ans = max(tmp, ans);
                    }

                    tmp = 0;
                    r = i, c = j;
                    while (r < N && c < M && r >= 0 && c >= 0)
                    {
                        tmp *= 10;
                        tmp += arr[r][c];
                        r -= k;
                        c -= l;
                        sqrttmp = static_cast<int>(sqrt(tmp));
                        if (sqrttmp * sqrttmp == tmp)
                            ans = max(tmp, ans);
                    }

                    tmp = 0;
                    r = i, c = j;
                    while (r < N && c < M && r >= 0 && c >= 0)
                    {
                        tmp *= 10;
                        tmp += arr[r][c];
                        r -= k;
                        c += l;
                        sqrttmp = static_cast<int>(sqrt(tmp));
                        if (sqrttmp * sqrttmp == tmp)
                            ans = max(tmp, ans);
                    }
                }
            }
        }
    }
    cout << ans << endl;

    return 0;
}