#include <stdio.h>
#include <stdlib.h>

int main(){

    int number = 0;
    printf("ENTER THE AMOUT OF GRADES YOU WANNA ENTER: ");
    scanf("%d",&number);

    char *grade = malloc(number * sizeof(char));

    if(grade == NULL){
        printf("ERROR");
        return 1;
    }

    for(int i = 0; i < number; i++){
        printf("ENTER THE #%d GRADE: ", i + 1);
        scanf(" %c",&grade[i]);
    }

    for(int i = 0; i < number; i++){
        printf("#%d GRADE: %c", i + 1, grade[i]);
        printf("\n");
    }


    free(grade);
    grade = NULL;

    return 0;
}