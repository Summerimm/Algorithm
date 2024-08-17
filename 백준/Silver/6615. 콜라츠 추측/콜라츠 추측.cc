#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll A, B, C;
    ll Sa, Sb;
    bool flag;
    vector<ll> v1;
    vector<ll> v2;

    while (true)
    {
        flag = false;

        v1.clear();
        v2.clear();

        cin >> A >> B;
        if (A == 0 && B == 0)
            break;

        int originA, originB;
        originA = A;
        originB = B;

        v1.push_back(A);
        v2.push_back(B);

        while (A != 1)
        {
            if (A % 2 == 1)
                A = A * 3 + 1;
            else
                A /= 2;
            v1.push_back(A);
        }

        while (B != 1)
        {
            if (B % 2 == 1)
                B = B * 3 + 1;
            else
                B /= 2;
            v2.push_back(B);
        }

        for (int i = 0; i < v1.size(); i++)
        {
            for (int j = 0; j < v2.size(); j++)
            {
                if (v1[i] == v2[j])
                {
                    Sa = i;
                    Sb = j;
                    C = v1[i];
                    flag = true;
                    break;
                }
            }
            if (flag)
                break;
        }
        cout << originA << " needs " << Sa << " steps, " << originB << " needs " << Sb << " steps, they meet at " << C << endl;
    }

    return 0;
}