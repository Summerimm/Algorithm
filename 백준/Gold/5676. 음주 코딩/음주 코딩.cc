#include <iostream>
#include <algorithm>

#define endl "\n"
#define INF int(1e9) + 1

using namespace std;

int N, M;
int arr[100001];

struct Node
{
    int x, y, z;
};

struct SegTree
{
    SegTree(){};
    Node tree[1 << 20];
    int base = 1;

    void init(int a[])
    {
        base = 1;
        while (base < N)
            base <<= 1;
        for (int i = N; i < base; i++)
            tree[base + i] = {0, 0, 0};
        base--;
        for (int i = 1; i <= N; i++)
        {
            if (arr[i] < 0)
                tree[base + i] = {1, 0, 0};
            else if (arr[i] == 0)
                tree[base + i] = {0, 1, 0};
            else
                tree[base + i] = {0, 0, 1};
        }
        for (int i = base; i > 0; i--)
            tree[i] = {tree[i << 1].x + tree[i << 1 | 1].x, tree[i << 1].y + tree[i << 1 | 1].y, tree[i << 1].z + tree[i << 1 | 1].z};
    }

    void update(int id, int k)
    {
        int tmp = base + id;
        if (k < 0)
            tree[tmp] = {1, 0, 0};
        else if (k == 0)
            tree[tmp] = {0, 1, 0};
        else
            tree[tmp] = {0, 0, 1};
        for (tmp >>= 1; tmp; tmp >>= 1)
            tree[tmp] = {tree[tmp << 1].x + tree[tmp << 1 | 1].x, tree[tmp << 1].y + tree[tmp << 1 | 1].y, tree[tmp << 1].z + tree[tmp << 1 | 1].z};
    }

    Node query(int id, int left, int right, int start, int end)
    {
        if (left > end || right < start)
            return {0, 0, 0};
        if (left <= start && end <= right)
            return tree[id];

        int mid = (start + end) / 2;
        Node left_v = query(id << 1, left, right, start, mid);
        Node right_v = query(id << 1 | 1, left, right, mid + 1, end);
        return {left_v.x + right_v.x, left_v.y + right_v.y, left_v.z + right_v.z};
    }
} T;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    while (cin >> N >> M)
    {
        for (int i = 1; i <= N; i++)
            cin >> arr[i];
        T.init(arr);

        char a;
        int b, c;
        for (int i = 0; i < M; i++)
        {
            cin >> a >> b >> c;
            if (a == 'C')
                T.update(b, c);
            else
            {
                Node node = T.query(1, b, c, 1, T.base + 1);
                if (node.y > 0)
                    cout << 0;
                else if (node.x % 2)
                    cout << "-";
                else
                    cout << "+";
            }
        }
        cout << endl;
    }

    return 0;
}