#include <iostream>
#include <math.h>

#define endl "\n"

using namespace std;

bool isPrime(int A)
{
    if (A < 2)
        return false;
    if (A == 2)
        return true;
    for (int i = 2; i < int(sqrt(A)) + 1; i++)
        if (A % i == 0)
            return false;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int arr[500];
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int prefixSum[500] = {
        0,
    };
    for (int i = 1; i < N + 1; i++)
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1];

    int ans = 0;
    for (int i = 1; i < N + 1; i++)
        for (int j = 0; j < i - 1; j++)
        {
            int a = prefixSum[i] - prefixSum[j];
            if (isPrime(i - j) && isPrime(a))
                ans++;
        }
    cout << ans << endl;
    return 0;
}