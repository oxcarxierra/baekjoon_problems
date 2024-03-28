#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> v(N);
    vector<int> sum(N + 1);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i];
    }
    sum[0] = 0;
    for (int i = 1; i <= N; i++)
    {
        sum[i] = sum[i - 1] + v[i - 1];
    }

    int INF = 2000 * N;
    vector<bool> isPrime(INF + 1, true);
    isPrime[0] = false;
    isPrime[1] = false;
    isPrime[2] = true;
    int i = 2;
    while (i * i <= INF)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j <= INF; j += i)
            {
                isPrime[j] = false;
            }
        }
        i++;
    }
    int cnt = 0;
    for (int i = 0; i < N + 1; i++)
    {
        for (int j = i + 1; j < N + 1; j++)
        {
            if (j - i > 1 && isPrime[sum[j] - sum[i]] && isPrime[j - i])
                cnt++;
        }
    }
    cout << cnt << endl;
}