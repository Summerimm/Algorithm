#include <iostream>
#include <iomanip>

using namespace std;

struct Line
{
    double A, B, C;
};

// 두 점을 받아 직선 방정식을 구하는 함수
Line getLine(int x1, int y1, int x2, int y2)
{
    Line line;
    line.A = y2 - y1;
    line.B = x1 - x2;
    line.C = line.A * x1 + line.B * y1;
    return line;
}

// 두 직선의 교차점을 구하는 함수
void solve(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4)
{
    Line l1 = getLine(x1, y1, x2, y2);
    Line l2 = getLine(x3, y3, x4, y4);

    double det = l1.A * l2.B - l1.B * l2.A;

    if (det == 0)
    {
        if (l1.A * l2.C == l2.A * l1.C && l1.B * l2.C == l2.B * l1.C)
            cout << "LINE" << endl;
        else
            cout << "NONE" << endl;
    }
    else
    {
        double x = (l2.B * l1.C - l1.B * l2.C) / det;
        double y = (l1.A * l2.C - l2.A * l1.C) / det;
        cout << "POINT " << fixed << setprecision(2) << x << " " << y << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    while (N--)
    {
        int x1, y1, x2, y2, x3, y3, x4, y4;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
        solve(x1, y1, x2, y2, x3, y3, x4, y4);
    }

    return 0;
}