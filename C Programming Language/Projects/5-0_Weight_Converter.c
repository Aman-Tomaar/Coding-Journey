#include <stdio.h>
#include <string.h>

int main(){

    char kg[10] = "kilogram";
    char pound[10] = "pound";
    float weight = 0.0f;
    char yourchoice[10] = "\0";

    printf("Enter the weight : ");
    scanf("%f", &weight);
    getchar(); // Clears the newline so fgets doesn't skip

    printf("You want to convert this value to? (kilogram, pound) : ");
    fgets(yourchoice, sizeof(yourchoice), stdin);
    yourchoice[strcspn(yourchoice, "\n")] = '\0';

    if(strcmp(yourchoice, kg) == 0){
        float converted = weight / 2.20462;
        printf("Result: %.2f kg\n", converted);
    }
    else if(strcmp(yourchoice, pound) == 0){
        float converted = weight * 2.20462;
        printf("Result: %.2f pounds\n", converted);
    }
    else {
        printf("Invalid choice!\n");
    }

    return 0;
}
