#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int N;
int arr[1000];
int incdp[1000];
int decdp[1000];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
        incdp[i] = 1;
        decdp[i] = 1;
    }

    for (int i = 0; i < N; i++)
        for (int j = i - 1; j > -1; j--)
            if (arr[j] < arr[i])
                incdp[i] = max(incdp[i], incdp[j] + 1);

    for (int i = N - 1; i > -1; i--)
        for (int j = i + 1; j < N; j++)
            if (arr[j] < arr[i])
                decdp[i] = max(decdp[i], decdp[j] + 1);

    int ans = 0;
    for (int i = 0; i < N; i++)
        ans = max(ans, incdp[i] + decdp[i]);
    cout << ans - 1 << endl;
    return 0;
}