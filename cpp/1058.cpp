#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> v(n);
    for (int i = 0; i < n; i++)
        string str = "";
    cin >> str;
    for (char c : str)
    {
        if (c == 'Y')
    }
    cin >> v[i];
    sort(v.begin(), v.end());
    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int x;
        cin >> x;
        cout << binary_search(v.begin(), v.end(), x) << '\n';
    }
    return 0;
}
