#include <stdio.h>

typedef enum {
    SUNDAY = 1, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, 
    FRIDAY, SATURDAY
}day;

typedef enum{
    success , failure , pending
}status;

int main(){

    day today = SUNDAY;
    if(today == SUNDAY || today == SATURDAY){
        printf("It's a Weakend\n");
    }
    else{
        printf("It's Weakday\n");
    }
    status connection = 2;
    if(connection == success){
        printf("CONNECTED SUCCESFULLY\n");
    }
    else if(connection == failure){
        printf("CONNECTION FAILED\n");
    }
    else{
        printf("CONNECTION IS ONGOING\n");
    }
    return 0;
}