#include <iostream>
#include <set>
using namespace std;

set<int> numbers(set<int> *v)
{
    set<int> new_v;
    for (auto i : *v)
    {
        new_v.insert(i + 1);
        new_v.insert(i + 5);
        new_v.insert(i + 10);
        new_v.insert(i + 50);
    }
    return new_v;
};

int main()
{
    set<int> v = {1, 5, 10, 50};
    int N = 0;
    cin >> N;
    for (int i = 1; i < N; i++)
    {
        v = numbers(&v);
    }
    cout << v.size() << endl;
}