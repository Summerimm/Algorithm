#include <iostream>
#include <algorithm>

#define endl "\n"
#define INF int(1e9) + 1

using namespace std;

int N, M, K;
int arr[100001];

struct SegTree
{
    SegTree(){};

    pair<int, int> tree[1 << 20];
    int base = 1;

    void init(int a[])
    {
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = {0, INF};
        base--;
        for (int i = 1; i <= N; i++)
            tree[base + i] = {arr[i], arr[i]};
        for (int i = base; i > 0; i--)
            tree[i] = {max(tree[i << 1].first, tree[i << 1 | 1].first), min(tree[i << 1].second, tree[i << 1 | 1].second)};
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        tree[tmp] = {k, k};
        for (tmp >>= 1; tmp; tmp >>= 1)
            tree[tmp] = {max(tree[tmp << 1].first, tree[tmp << 1 | 1].first), min(tree[tmp << 1].second, tree[tmp << 1 | 1].second)};
    }

    pair<int, int> query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return {0, INF};
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        pair<int, int> left_v = query(id << 1, left, right, start, mid);
        pair<int, int> right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return {max(left_v.first, right_v.first), min(left_v.second, right_v.second)};
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        cin >> arr[i];
    T.init(arr);

    int a, b, c;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        pair<int, int> pii = T.query(1, a, b, 1, T.base + 1);
        cout << pii.first - pii.second << endl;
    }

    return 0;
}