#include <iostream>
#include <algorithm>

#define endl "\n"
#define INF int(1e9)

using namespace std;

int N, q;
int arr[100000];

struct SegTree
{
    SegTree(){};

    int tree[1 << 18];
    int base = 1;

    void init(int a[])
    {
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = INF;
        for (int i = 0; i < N; i++)
            tree[base + i] = arr[i];
        base--;
        for (int i = base; i > 0; i--)
            tree[i] = min(tree[i << 1], tree[i << 1 | 1]);
    }

    int query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return INF;
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        int left_min = query(id << 1, left, right, start, mid);
        int right_min = query(id << 1 | 1, left, right, mid + 1, end);
        return min(left_min, right_min);
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> q;
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    T.init(arr);

    int left, right;
    for (int i = 0; i < q; i++)
    {

        cin >> left >> right;
        cout << T.query(1, left, right, 1, T.base + 1) << endl;
    }
    return 0;
}