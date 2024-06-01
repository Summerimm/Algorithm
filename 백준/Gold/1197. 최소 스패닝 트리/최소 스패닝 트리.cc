#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

struct Node
{
    int w;
    int a;
    int b;
};

bool cmp(Node &x, Node &y)
{
    return x.w < y.w;
}

int V, E;
int a, b, w;
int parent[10001];
vector<Node> v;
int ans;

int find(int a)
{
    if (parent[a] == a)
        return a;
    return parent[a] = find(parent[a]);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> V >> E;
    for (int i = 0; i < E; i++)
    {
        cin >> a >> b >> w;
        v.push_back({w, a, b});
    }

    for (int i = 1; i <= V; i++)
        parent[i] = i;

    sort(v.begin(), v.end(), cmp);

    ans = 0;
    for (auto vec : v)
    {
        int pa = find(vec.a);
        int pb = find(vec.b);
        if (pa != pb)
        {
            parent[pb] = pa;
            ans += vec.w;
        }
    }
    cout << ans << endl;
    return 0;
}