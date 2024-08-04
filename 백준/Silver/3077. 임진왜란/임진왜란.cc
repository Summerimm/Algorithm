#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<string> v;
    unordered_map<string, int> um;
    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        v.push_back(str);
    }

    for (int i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        um[str] = i;
    }

    int ans = 0;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (um[v[i]] < um[v[j]])
                ans++;
        }
    }
    cout << ans << "/" << (N * (N - 1) / 2) << endl;

    return 0;
}