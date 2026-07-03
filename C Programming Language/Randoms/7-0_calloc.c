#include <stdio.h>
#include <stdlib.h>

int main(){

    int player = 0;
    printf("ENTER THE NUMBER OF PLAYER(s): ");
    scanf("%d",&player);

    int *score = calloc(player , sizeof(int));

    if(score == NULL){
        printf("ERROR");
        return 1;
    }

    for(int i = 0; i < player; i++ ){
        printf("ENTER THE SCORE OF #%d PLAYER: ",i+1);
        scanf("%d",&score[i]);
    }
    for(int i = 0; i < player; i++ ){
        printf("THE SCORE OF #%d PLAYER: %d\n", i + 1 , score[i]);
    }


    score = NULL;
    free(score);
    return 0;
}