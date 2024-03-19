#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int num;
    int ans = 0;
    cin >> num;
    string str_num = to_string(num);
    sort(str_num.begin(), str_num.end());

    do
    {
        if (str_num[0] == '0')
            continue;
        int a = stoi(str_num);
        // cout << a << endl;
        if (a > num)
        {
            if (ans > a || ans == 0)
            {
                ans = a;
            }
        }
    } while (next_permutation(str_num.begin(), str_num.end()));
    cout << ans << endl;
}