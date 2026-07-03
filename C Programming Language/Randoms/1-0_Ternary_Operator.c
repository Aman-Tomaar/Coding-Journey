#include <stdio.h>
#include <stdbool.h>
int main(){

    int x =7;
    int y = 8;
    printf("CASE I => MAX NUMBER IS: %d\n\n", (x > y) ? x : y );

    bool isonline = true;
    printf("CASE II => %s\n\n", (isonline == 1) ? "YES I AM ONLINE" : "NO I AM OFFLINE");

    int num = 0;
    printf("CASE III =>\nENTER THE NUBER: ");
    scanf("%d",&num);
    printf("THE NUMBER %d IS %s\n\n", num , (num % 2 == 0) ? "EVEN" : "ODD");

    int age = 0;
    printf("CASE IV =>\nENTER YOUR AGE: ");
    scanf("%d",&age);
    printf("YOU ARE %d YEAR(s) OLD , HENCE YOU ARE %s", age , (age > 18) ? "ELIGIBLE" : "NOT ELIGIBLE");


    return 0;
}   