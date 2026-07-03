#include <iostream>

namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}
int main(){
    using std::cout;
    /*
    using std namespace std; => for everything (remove std from whole code)

    using std::string; => for std::string << .......... ;

    using namespace first;
    std::cout << x << '\n'; O/P = 1
    
    int x = 0;
    std::cout << x << '\n'; O/P = 0
    */
    cout << first::x << '\n';
    cout << second::x << '\n';

    return 0;
}