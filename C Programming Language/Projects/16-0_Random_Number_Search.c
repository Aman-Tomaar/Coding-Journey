#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <windows.h>

int main(){

    // Seed the random number generator using the current time
    srand(time(NULL));

    printf("Searching for the number 99...\n");

    while(true){
        int min = 50;
        int max = 100;

        // Generate number between 50 and 100
        int randomnum = (rand() % (max - min + 1)) + min;

        Sleep(100); // Pause for 100 milliseconds
        printf("%d ", randomnum);

        if(randomnum == 99){
            printf("\n\nFound 99! Stopping the search.\n");
            break;
        }
    }

    return 0;
}