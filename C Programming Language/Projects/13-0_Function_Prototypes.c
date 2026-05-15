#include <stdio.h>
#include <stdbool.h>

// Function Prototype (The "Announcement")
bool agecheck(int num);

int main(){
    int age = 17;

    if(agecheck(age)){
        printf("You are 18 years old\n");
    }
    else{
        printf("You are not 18 years old\n");
    }

    return 0;
}

// Function Definition (The "Instructions")
bool agecheck(int num){
    if(num >= 18){
        return true;
    }
    else{
        return false;
    }
}