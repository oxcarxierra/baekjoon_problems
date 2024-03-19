#include <iostream>
#include <set>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N = 0;
    int cnt = 0;
    cin >> N;
    cin.ignore();
    set<string> people;
    for (int i = 0; i < N; i++)
    {
        string id = "";
        getline(cin, id);
        if (id == "ENTER")
        {
            people.clear();
            continue;
        }
        if (people.find(id) == people.end())
        {
            cnt++;
            people.insert(id);
        }
    }
    cout << cnt << endl;
    return 0;
}