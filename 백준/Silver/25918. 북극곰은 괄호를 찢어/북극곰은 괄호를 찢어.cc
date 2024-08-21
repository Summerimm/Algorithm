#include <iostream>
#include <stack>

#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    string str;
    cin >> str;

    int ans = 0;
    stack<char> st;
    int sz;
    for (int i = 0; i < str.length(); i++)
    {
        if (st.empty())
            st.push(str[i]);
        else if (st.top() == '(' && str[i] == ')')
            st.pop();
        else if (st.top() == ')' && str[i] == '(')
            st.pop();
        else
            st.push(str[i]);
        sz = st.size();
        ans = ans >= sz ? ans : sz;
    }

    if (!st.empty())
        cout << -1 << endl;
    else
        cout << ans << endl;
    return 0;
}