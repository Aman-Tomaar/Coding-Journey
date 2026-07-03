#include <iostream>
int main(){

    //Whole Number
    int x = 5;
    int y = 6;
    std::cout << x << '\n';
    std::cout << y << '\n';
    std::cout << x + y << '\n';

    //Number with Decimals
    double price = 10.99;
    std::cout << price << '\n';

    //Single Character
    char grade = 'A';
    std::cout << grade << '\n';

    //Boolean
    bool isRunning = true;
    std::cout << isRunning << '\n';

    //String (Multiple Characters)
    std::string name = "BOB";
    std::cout << name << '\n';


    std::cout << "X--------------------------------X" << '\n';
    std::cout << "STUDENT NAME IS " << name << '\n';
    std::cout << "HIS FAV NUMBER IS " << x + y << '\n';
    std::cout << "HIS GRADE IS " << grade << '\n';
    std::cout << "HE IS A GOOD BOY 1 => YES 2 => NO SO HE'S A " << isRunning << '\n';
    std::cout << "X--------------------------------X" << '\n';
    return 0;
}