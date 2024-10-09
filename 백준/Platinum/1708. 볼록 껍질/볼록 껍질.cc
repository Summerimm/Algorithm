#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define endl "\n"

using namespace std;

struct Coor
{
    long long x, y;
};

vector<Coor> Point;

long long CCW(Coor a, Coor b, Coor c)
{
    return a.x * b.y + b.x * c.y + c.x * a.y - a.x * c.y - b.x * a.y - c.x * b.y;
}

bool cmp(Coor a, Coor b)
{
    long long Value = CCW(Point[0], a, b);
    if (Value)
        return Value > 0;
    else if (a.y != b.y)
        return a.y < b.y;
    else
        return a.x < b.x;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    Coor temp1, temp2;
    stack<Coor> Convex;

    cin >> N;
    Point.resize(N);
    for (int i = 0; i < N; i++)
        cin >> Point[i].x >> Point[i].y;

    // Point[0]에 가장 왼쪽 아래에 위치한 좌표 넣기
    for (int i = 0; i < N; i++)
        if (Point[i].y < Point[0].y || (Point[i].y == Point[0].y && Point[i].x < Point[0].x))
            swap(Point[0], Point[i]);

    sort(Point.begin() + 1, Point.end(), cmp);
    Convex.push(Point[0]);
    Convex.push(Point[1]);
    for (int i = 2; i < N; i++)
    {
        while (Convex.size() >= 2)
        {
            temp2 = Convex.top();
            Convex.pop();
            temp1 = Convex.top();
            if (CCW(temp1, temp2, Point[i]) > 0)
            {
                Convex.push(temp2);
                break;
            }
        }
        Convex.push(Point[i]);
    }

    cout << Convex.size() << endl;

    return 0;
}