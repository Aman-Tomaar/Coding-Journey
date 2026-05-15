#include <stdio.h>
#include <string.h> 

int main(){

    int age = 0;
    float GPA = 0.0;
    char grade = '0';
    char name[20] = "";

    printf("Enter age = ");
    scanf("%d", &age);

    printf("Enter GPA = ");
    scanf("%f", &GPA);

    printf("Enter grade = ");
    scanf(" %c",&grade);

    getchar(); 
    printf("Enter name = ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; 

    printf("name = %s\n", name);
    printf("age = %d\n", age);
    printf("GPA = %.2f\n", GPA);
    printf("grade = %c\n", grade);

    return 0;

}