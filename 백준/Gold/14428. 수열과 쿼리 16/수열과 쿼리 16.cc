#include <iostream>
#include <algorithm>

#define endl "\n"
#define INF int(1e10)

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
            tree[base + i] = {INF, i};
        base--;
        for (int i = 1; i <= N; i++)
            tree[base + i] = {arr[i], i};
        for (int i = base; i > 0; i--)
        {
            if (tree[i << 1].first <= tree[i << 1 | 1].first)
                tree[i] = {tree[i << 1].first, tree[i << 1].second};
            else
                tree[i] = {tree[i << 1 | 1].first, tree[i << 1 | 1].second};
        }
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        tree[tmp].first = k;
        for (tmp >>= 1; tmp; tmp >>= 1)
        {
            if (tree[tmp << 1].first <= tree[tmp << 1 | 1].first)
                tree[tmp] = {tree[tmp << 1].first, tree[tmp << 1].second};
            else
                tree[tmp] = {tree[tmp << 1 | 1].first, tree[tmp << 1 | 1].second};
        }
    }

    pair<int, int> query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return {INF, INF};
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        pair<int, int> left_v = query(id << 1, left, right, start, mid);
        pair<int, int> right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return left_v.first <= right_v.first ? left_v : right_v;
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> arr[i];
    T.init(arr);

    cin >> M;
    int a, b, c;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> c;
        if (a == 1)
            T.update(b, c);
        else
            cout << T.query(1, b, c, 1, T.base + 1).second << endl;
    }

    return 0;
}