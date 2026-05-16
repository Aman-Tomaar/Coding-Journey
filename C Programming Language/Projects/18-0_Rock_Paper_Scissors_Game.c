#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int win , loose = 0;
int score = 0;

int getuserchoice();
int getcompchoice();
void checkwinner(int userchoice,int compchoice);

int main(){

    char c = '\0';

    score = win - loose;

    printf("**** ROCK PAPER SCISSORS ****\n");
    do{
        srand (time(NULL));

        int compchoice = getcompchoice();
        int userchoice = getuserchoice();

        switch(userchoice){
            case 1:
                printf("You chose ROCK!\n");
                break;
            case 2:
                printf("You chose PAPER!\n");
                break;
            case 3:
                printf("You chose SCISSORS!\n");
                break;
        }

        switch(compchoice){
            case 1:
                printf("Computer chose ROCK!\n");
                break;
            case 2:
                printf("Computer chose PAPER!\n");
                break;
            case 3:
                printf("Computer chose SCISSORS!\n");
                break;
        }

        checkwinner(userchoice , compchoice);

        printf("DO U WANT TO PLAY AGAIN (Y/N): ");
        scanf(" %c" , &c);

    }while( c == 'Y' || c == 'y');

    printf("**** GAME ENDED ****\n");
    printf("X-----------------X\n");
    printf("TOTAL WIN: %d\nTOTAL LOSE: %d\nSO YOU HAVE SCORED: %d\n", win , loose ,score);
    printf("X-----------------X\n");

    return 0;
}


int getuserchoice(){
    int choice = 0;

    do{
        printf("1. ROCK\n");
        printf("2. PAPER\n");
        printf("3. SCISSORS\n");
        printf("Choose 1/2/3: ");
        scanf("%d", &choice);
    }while(choice < 1 || choice > 3);

    return choice;
}

int getcompchoice(){
    return (rand() % 3) + 1;
}

void checkwinner(int userchoice,int compchoice){

    printf("X-----------------X\n");
    printf("**** RESULTS *****\n");
    
    if(userchoice == compchoice){
        printf("IT's A TIE!\n");
    }
    else if( userchoice == 1 && compchoice == 3 || userchoice == 2 && compchoice == 1 || userchoice == 3 && compchoice == 2){
        printf("YOU WIN!\n");
        win++;
    }
    else{
        printf("YOU LOOSE!\n");
        loose++;  
    }
    printf("X-----------------X\n");
}