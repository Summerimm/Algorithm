#include <iostream>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string tmp = "";
    string str;
    getline(cin, str);

    int N = str.length();

    for (int i = 0; i < N; i++)
    {
        if (str[i] == ' ')
            if (tmp == "")
                continue;
            else
            {
                cout << tmp << " ";
                tmp = "";
            }
        else
        {
            if (str[i] == '<' || str[i] == '>' || str[i] == '(' || str[i] == ')')
            {
                if (tmp == "")
                    cout << str[i] << " ";
                else
                {
                    cout << tmp << " " << str[i] << " ";
                    tmp = "";
                }
            }
            else if (str[i] == '&')
            {
                if (tmp == "")
                    cout << "&&" << " ";
                else
                {
                    cout << tmp << " " << "&&" << " ";
                    tmp = "";
                }
                i++;
            }
            else if (str[i] == '|')
            {
                if (tmp == "")
                    cout << "||" << " ";
                else
                {
                    cout << tmp << " " << "||" << " ";
                    tmp = "";
                }
                i++;
            }
            else
                tmp += str[i];
        }
    }
    if (tmp != " ")
        cout << tmp << endl;
    return 0;
}