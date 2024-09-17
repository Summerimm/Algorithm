#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    string str;
    cin >> N >> str;
    for (int i = 0; i < N; i++)
        cout << str;
    cout << endl;
    return 0;
}