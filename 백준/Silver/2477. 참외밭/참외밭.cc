#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int K;
    int W = 0, H = 0, sW, sH;
    int idx1, idx2;
    int a, b;
    int arr[6];

    cin >> K;
    for (int i = 0; i < 6; i++)
    {
        cin >> a >> b;
        arr[i] = b;
    }

    for (int i = 0; i < 6; i++)
    {
        if (i % 2)
        {
            if (H < arr[i])
            {
                H = arr[i];
                idx1 = i;
            }
        }
        else
        {
            if (W < arr[i])
            {
                W = arr[i];
                idx2 = i;
            }
        }
    }

    int idx;
    if (idx1 == 5 && idx2 == 0)
        idx = idx1;
    else if (idx1 == 0 && idx2 == 5)
        idx = idx2;
    else
        idx = min(idx1, idx2);
    sW = arr[(idx + 3) % 6];
    sH = arr[(idx + 4) % 6];

    cout << (W * H - sW * sH) * K << endl;
    return 0;
}