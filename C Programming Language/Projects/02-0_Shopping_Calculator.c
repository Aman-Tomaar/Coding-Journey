#include <stdio.h>
#include <string.h>

int main(){

    char item[50]="\0";
    float price=0.0f;
    int quantity=0;
    char currency='$';
    float total=0.0f;

    printf("What do you want to buy : ");
    fgets(item,sizeof(item),stdin);
    
    item[strcspn(item, "\n")] = 0; 

    printf("Enter the price of 1 X %s : ",item);
    scanf("%f",&price);

    printf("Enter the amount of %s you are buying : ",item);
    scanf("%d",&quantity);

    total = price * quantity;

    printf("X--------------------------------------X\nYou are buying %d X %s\nAt the price of %.2f each\nThe total would be %.2f :)\nHave a good day!!! Come back later!", quantity, item, price, total);

    return 0;
}