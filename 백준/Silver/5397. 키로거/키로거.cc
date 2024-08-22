#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--)
    {
        string str;
        cin >> str;

        stack<char> leftStack, rightStack;

        for (char c : str)
        {
            if (c == '<')
            {
                if (!leftStack.empty())
                {
                    rightStack.push(leftStack.top());
                    leftStack.pop();
                }
            }
            else if (c == '>')
            {
                if (!rightStack.empty())
                {
                    leftStack.push(rightStack.top());
                    rightStack.pop();
                }
            }
            else if (c == '-')
            {
                if (!leftStack.empty())
                {
                    leftStack.pop();
                }
            }
            else
            {
                leftStack.push(c);
            }
        }

        // 왼쪽 스택에 있는 문자들을 모두 오른쪽 스택으로 이동
        while (!leftStack.empty())
        {
            rightStack.push(leftStack.top());
            leftStack.pop();
        }

        // 오른쪽 스택에 있는 문자들을 출력
        while (!rightStack.empty())
        {
            cout << rightStack.top();
            rightStack.pop();
        }

        cout << '\n';
    }

    return 0;
}
