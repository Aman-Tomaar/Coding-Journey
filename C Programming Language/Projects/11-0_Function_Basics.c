#include <stdio.h>
#include <string.h>

// Function definition
void happy(char name[], int age){
    printf("\n--- Greeting ---\n");
    printf("Name: %s\nAge: %d\n", name, age);
}

int main(){

    char name[40] = "\0";
    int age = 0;

    printf("Enter name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0'; // Safer newline removal

    printf("Enter age: ");
    scanf("%d", &age);

    // Calling the function and passing 'arguments'
    happy(name, age);

    return 0;
}