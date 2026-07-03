#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    srand(time(NULL));

    int min = 1;
    int max = 100;
    int guess = 0;
    int tries = 0;
    int randnum = (rand() % (max - min + 1)) + min;

    printf("**** NUMBER GUESSING GAME ****\n");
    printf("**** NUMBER IS BETWEEN %d-%d ****\n",min,max);

    while(1){
        printf("GUESS THE NUMBER : ");
        scanf("%d",&guess);
        tries++;
        if(guess > randnum){
            printf("NUMER IS LESS THAN %d\n\n", guess);
        }
        else if(guess < randnum){
            printf("NUMBER IS GREATER THAN %d\n\n", guess);
        }
        else if(guess == randnum){
            printf("**** CONGRATULATIONS ****\n");
            printf("YOU HAVE GUESSED THE NUMBER CORRECTY\n");
            printf("NUMBER WAS %d\n",randnum);
            printf("IT TOOK YOU %d TRY(s)",tries);
            break;
        }

    }
    return 0;
}