#include <stdio.h>

int main(){

    float num1 = 0.0f;
    float num2 = 0.0f;
    char opp = '\0';
    float ans = 0.0f;

    printf("Enter two numbers: ");
    scanf("%f", &num1);
    scanf("%f", &num2);
    
    getchar(); // Consumes the newline left by the last scanf
    
    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &opp);

    switch(opp){
        case '+':
            ans = num1 + num2;
            printf("+ : %.2f\n", ans); 
            break;
        case '-':
            ans = num1 - num2;
            printf("- : %.2f\n", ans); 
            break;
        case '*':
            ans = num1 * num2;
            printf("* : %.2f\n", ans); 
            break;
        case '/':
            if(num2 != 0) {
                ans = num1 / num2;
                printf("/ : %.2f\n", ans);
            } else {
                printf("Error: Division by zero!\n");
            }
            break;
        default:
            printf("BYE\n");
    }

    return 0;
}