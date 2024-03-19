#include <iostream>
using namespace std;

int main()
{
    int N = 0;
    int num = 666;
    cin >> N;
    while (true)
    {
        string s = to_string(num);
        if (s.find("666") != string::npos)
        {
            N--;
        }
        if (N == 0)
        {
            cout << num << endl;
            break;
        }
        num++;
    }
}