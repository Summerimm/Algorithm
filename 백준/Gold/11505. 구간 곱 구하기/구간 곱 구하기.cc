#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int N, M, K;
int arr[1000000];

struct SegTree
{
    SegTree(){};

    long long tree[1 << 21];
    int base = 1;

    void init(int a[])
    {
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = 1;
        for (int i = 0; i < N; i++)
            tree[base + i] = arr[i];
        base--;
        for (int i = base; i > 0; i--)
            tree[i] = tree[i << 1] * tree[i << 1 | 1] % 1000000007;
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        tree[tmp] = k;
        for (tmp >>= 1; tmp; tmp >>= 1)
            tree[tmp] = tree[tmp << 1] * tree[tmp << 1 | 1] % 1000000007;
    }

    int query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return 1;
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        long long left_v = query(id << 1, left, right, start, mid);
        long long right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return left_v * right_v % 1000000007;
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> K;
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    T.init(arr);

    int a, b, c;
    for (int i = 0; i < M + K; i++)
    {
        cin >> a >> b >> c;
        if (a == 1)
            T.update(b, c);
        else
            cout << T.query(1, b, c, 1, T.base + 1) << endl;
    }

    return 0;
}