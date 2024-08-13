#include <iostream>
#include <string>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    string str;
    char next1;
    char next2;
    cin >> N;
    for (int t = 0; t < N; t++)
    {
        bool flag = true;
        cin >> str;
        int len = str.length();
        for (int i = 0; i < len - 1; i++)
        {
            if (i == 0)
            {
                if (str[i] == 'A')
                {
                    next1 = 'A';
                    next2 = 'F';
                }
                else if (str[i] == 'B' || str[i] == 'C' || str[i] == 'D' || str[i] == 'E' || str[i] == 'F')
                {
                    next1 = 'A';
                    next2 = 'A';
                }
                else
                {
                    cout << "Good" << endl;
                    flag = false;
                    break;
                }
            }
            else if (str[i] != next1 && str[i] != next2)
            {
                cout << "Good" << endl;
                flag = false;
                break;
            }
            else if (str[i] == 'A')
            {
                next1 = 'A';
                next2 = 'F';
            }
            else if (str[i] == 'F')
            {
                next1 = 'F';
                next2 = 'C';
            }
            else if (str[i] == 'C')
            {
                next1 = 'C';
                next2 = 'C';
            }
        }

        if (flag)
        {
            if (str[len - 1] == 'A' || str[len - 1] == 'B' || str[len - 1] == 'C' || str[len - 1] == 'D' || str[len - 1] == 'E' || str[len - 1] == 'F')
                cout << "Infected!" << endl;
            else
                cout << "Good" << endl;
        }
        // 시작은 {A, B, C, D, E, F} 중 하나거나 0개
        // A가 아니라면 다음은 A여야 함
        // A뒤에는 A, F
        // F뒤에는 F, C
        // C뒤에는 C
        // 마지막은 {A, B, C, D, E, F} 중 하나거나 0개
    }
    return 0;
}