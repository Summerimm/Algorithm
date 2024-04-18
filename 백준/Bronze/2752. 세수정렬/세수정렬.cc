#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int arr[3];
int main()
{
    for (int i = 0; i < 3; i++)
        cin >> arr[i];

    sort(begin(arr), end(arr));

    for (int i = 0; i < 3; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}