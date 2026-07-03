#include <stdio.h>
#include <string.h>

int main() {
    char name[50] = "";

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    // The loop keeps running as long as the name is empty
    while (strlen(name) == 0) {
        printf("You must enter a name! Please try again: ");
        fgets(name, sizeof(name), stdin);
        name[strcspn(name, "\n")] = '\0';
    }

    printf("Hi %s\n", name);

    return 0;
}