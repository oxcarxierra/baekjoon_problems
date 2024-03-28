#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<string> trees;
    string tree;
    while (cin >> tree)
    {
        trees.push_back(tree);
    }
    sort(trees.begin(), trees.end());
    string prev = "";
    int count = 0;
    for (int i = 0; i < trees.size(); i++)
    {
        if (prev != trees[i])
        {
            if (prev != "")
            {
                cout << prev << " " << (double)count / trees.size() * 100 << "\n";
            }
            prev = trees[i];
            count = 1;
        }
        else
        {
            count++;
        }
    }
    cout << prev << " " << (double)count / trees.size() * 100 << "\n";
}