#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int max_person = 1;
    int max_number = 0;
    for (int i = 0; i < N; i++)
    {
        vector<int> cards(5);
        int max_sum = 0;
        for (int j = 0; j < 5; j++)
        {
            scanf(" %d", &cards[j]);
        }
        for (int j = 0; j < 3; j++)
        {
            for (int k = j + 1; k < 4; k++)
            {
                for (int l = k + 1; l < 5; l++)
                {
                    int sum = cards[j] + cards[k] + cards[l];
                    sum %= 10;
                    if (sum > max_sum)
                    {
                        max_sum = sum;
                    }
                }
            }
        }
        if (max_sum >= max_number)
        {
            max_number = max_sum;
            max_person = i + 1;
        }
    }
    cout << max_person << endl;
}