#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int N, M;

struct SegTree
{
    SegTree(){};

    long tree[1 << 21];
    int base = 1;

    void init()
    {
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = 0;
        base--;
        for (int i = 1; i <= N; i++)
            tree[base + i] = 0;
        for (int i = base; i > 0; i--)
            tree[i] = 0;
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        tree[tmp] += k;
        for (tmp >>= 1; tmp; tmp >>= 1)
            tree[tmp] = tree[tmp << 1] + tree[tmp << 1 | 1];
    }

    long query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return 0;
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        long left_v = query(id << 1, left, right, start, mid);
        long right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return left_v + right_v;
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    T.init();

    int a, b, c;
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> c;
        if (a == 1)
            T.update(b, c);
        else
            cout << T.query(1, b, c, 1, T.base + 1) << endl;
    }

    return 0;
}