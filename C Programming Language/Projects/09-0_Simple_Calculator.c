#include <stdio.h>

int main(){

    float num1 = 0.0f;
    float num2 = 0.0f;
    char opp = '\0';
    float ans = 0.0f;

    printf("Enter first number: ");
    scanf("%f", &num1);
    printf("Enter second number: ");
    scanf("%f", &num2);
    
    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &opp); // Note the space before %c

    switch(opp){
        case '+':
            ans = num1 + num2;
            printf("Result: %.2f\n", ans); 
            break;
        case '-':
            ans = num1 - num2;
            printf("Result: %.2f\n", ans); 
            break;
        case '*':
            ans = num1 * num2;
            printf("Result: %.2f\n", ans); 
            break;
        case '/':
            if(num2 != 0){
                ans = num1 / num2;
                printf("Result: %.2f\n", ans);
            } else {
                printf("Error: Division by zero!\n");
            }
            break;
        default:
            printf("Error: Invalid operator!\n");
    }

    return 0;
}