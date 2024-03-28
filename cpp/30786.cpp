#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N = 0;
    cin >> N;
    vector<pair<int, int>> v(N);
    vector<int> odd(N);
    vector<int> even(N);
    for (int i = 0; i < N; i++)
    {
        cin >> v[i].first >> v[i].second;
    }
    for (int i = 0; i < N; i++)
    {
        if (v[i].first + v[i].second % 2 == 0)
            even.push_back(i);
        else
            odd.push_back(i);
    }
    if (abs(odd.size() - even.size()) > 1)
    {
        cout << "NO" << endl;
        return 0;
    }
    for (int i = 0; i < N; i++)
    {
    }
}