#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> scores(N);
    for (int i = 0; i < N; i++)
    {
        scanf(" %d", &scores[i]);
    }
    int sum_score = 0;
    int max_score = 0;
    for (auto &score : scores)
    {
        sum_score += score;
        if (score > max_score)
            max_score = score;
    }
    float new_average = sum_score / static_cast<float>(max_score) * 100 / N;
    cout << new_average << endl;
}
