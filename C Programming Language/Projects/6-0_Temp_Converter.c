#include <stdio.h>

int main(){

    char choice = '\0';
    float f = 0.0f;
    float c = 0.0f;

    printf("WELCOME TO THE CELSIUS [C] TO FAHRENHEIT [F] CONVERTER PROGRAM :) \nChoose C or F : ");
    scanf("%c", &choice);

    if(choice == 'c' || choice == 'C'){
        printf("Enter Fahrenheit: ");
        scanf("%f", &f);
        c = (f - 32) * 5 / 9; // Actual formula
        printf("Celsius = %.2f\n", c);
    }
    else if(choice == 'f' || choice == 'F'){
        printf("Enter Celsius: ");
        scanf("%f", &c);
        f = (c * 9 / 5) + 32; // Actual formula
        printf("Fahrenheit = %.2f\n", f);
    }
    else{
        printf("Invalid choice!\n");
    }

    return 0;
}