#include <iostream>
#include <algorithm>

#define endl "\n"

using namespace std;

int arr[3];
int main()
{
  for (int i = 0; i < 3; i++) cin >> arr[i];
  sort(begin(arr), end(arr));
  cout << arr[1] << endl;
  return 0;
}