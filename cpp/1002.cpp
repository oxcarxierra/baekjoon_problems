#include <cmath>
#include <iostream>
using namespace std;

float dist(float x1, float y1, float x2, float y2)
{
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int get_points(float d, float r1, float r2)
{

    if (d == 0.0f)
    {
        if (r1 == r2)
            return -1;
        else
            return 0;
    }
    if (r1 + r2 < d)
        return 0;
    if (r1 + r2 == d)
        return 1;
    else
    {
        if (abs(r2 - r1) == d)
            return 1;
        if (abs(r2 - r1) > d)
            return 0;
        else
            return 2;
    }
}

int main()
{
    int T = 0;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        float x1, y1, r1, x2, y2, r2;
        scanf("%f %f %f %f %f %f", &x1, &y1, &r1, &x2, &y2, &r2);
        float d = dist(x1, y1, x2, y2);
        cout << get_points(d, r1, r2) << endl;
    }
}
