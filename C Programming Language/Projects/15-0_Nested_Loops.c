#include <stdio.h>
#include <string.h>

int main(){

    int c = 0;
    int r = 0;
    char s[50] = "\0";

    printf("Enter number of Rows (R): ");
    scanf("%d", &r);

    printf("Enter number of Columns (C): ");
    scanf("%d", &c);

    getchar(); // Clear the buffer before fgets

    printf("Enter the symbol or string to repeat: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';

    // Outer loop handles the rows
    for(int i = 0; i < r; i++){
        // Inner loop handles the columns
        for(int j = 0; j < c; j++){
            printf("%s ", s); // Added a space for better visibility
        }
        printf("\n"); // Move to the next line after finishing a row
    }

    return 0;
}