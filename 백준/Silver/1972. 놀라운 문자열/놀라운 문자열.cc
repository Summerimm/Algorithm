#include <iostream>
#include <unordered_map>
#include <set>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    set<string> arr[100];
    string str;
    while (true)
    {
        for (int i = 0; i < 100; i++)
            arr[i].clear();

        cin >> str;
        if (str == "*")
            break;

        int N = str.length();

        for (int i = 0; i < N - 1; i++)
        {
            string tmp = "";
            tmp += str[i];
            for (int j = i + 1; j < N; j++)
                arr[j - i - 1].insert(tmp + str[j]);
        }

        bool flag = true;
        for (int i = 0; i < N - 2; i++)
        {
            if (arr[i].size() != N - i - 1)
            {
                flag = false;
                break;
            }
        }

        if (flag)
            cout << str << " is surprising." << endl;
        else
            cout << str << " is NOT surprising." << endl;
    }

    return 0;
}