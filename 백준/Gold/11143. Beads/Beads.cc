#include <iostream>
#include <algorithm>

#define endl "\n"
#define INF int(1e9)

using namespace std;

int N, M, K;

struct SegTree
{
    SegTree(){};

    int tree[1 << 20];
    int base = 1;

    void init()
    {
        base = 1;
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = 0;
        for (int i = 0; i < N; i++)
            tree[base + i] = 0;
        base--;
        for (int i = base; i > 0; i--)
            tree[i] = tree[i << 1] + tree[i << 1 | 1];
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        tree[tmp] += k;
        for (tmp >>= 1; tmp; tmp >>= 1)
            tree[tmp] = tree[tmp << 1] + tree[tmp << 1 | 1];
    }

    int query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return 0;
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        int left_v = query(id << 1, left, right, start, mid);
        int right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return left_v + right_v;
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> N >> M >> K;
        T.init();

        char a;
        int b, c;
        for (int i = 0; i < M + K; i++)
        {
            cin >> a >> b >> c;
            if (a == 'P')
                T.update(b, c);
            else
                cout << T.query(1, b, c, 1, T.base + 1) << endl;
        }
    }

    return 0;
}