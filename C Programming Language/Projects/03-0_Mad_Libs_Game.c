#include <stdio.h>
#include <string.h>

int main() {

    char noun[50] = "";
    char verb[50] = "";
    char adj1[50] = "";
    char adj2[50] = "";
    char adj3[50] = "";

    printf("Enter the noun : ");
    fgets(noun, sizeof(noun), stdin);
    noun[strcspn(noun, "\n")] = '\0';

    printf("Enter the verb : ");
    fgets(verb, sizeof(verb), stdin);
    verb[strcspn(verb, "\n")] = '\0';

    printf("Enter the 1st adjective : ");
    fgets(adj1, sizeof(adj1), stdin);
    adj1[strcspn(adj1, "\n")] = '\0';

    printf("Enter the 2nd adjective : ");
    fgets(adj2, sizeof(adj2), stdin);
    adj2[strcspn(adj2, "\n")] = '\0';

    printf("Enter the 3rd adjective : ");
    fgets(adj3, sizeof(adj3), stdin);
    adj3[strcspn(adj3, "\n")] = '\0';

    printf("\n--- Your Story ---\n");
    printf("%s\n%s\n%s\n%s\n%s\n", noun, verb, adj1, adj2, adj3);

    return 0;
}