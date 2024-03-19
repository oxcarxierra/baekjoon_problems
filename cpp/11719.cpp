#include <iostream>
#include <string>

int32_t main()
{
    std::string str;
    for (int i = 0; i < 100; i++)
    {
        getline(std::cin, str);
        std::cout << str << std::endl;
    }
    return 0;
}