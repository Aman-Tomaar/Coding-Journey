#include <stdio.h>
#include <stdbool.h>

// Function that returns a boolean value
bool agecheck(int num){
    if(num >= 18){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int age = 17;

    // The function call 'agecheck(age)' is replaced by its return value (true/false)
    if(agecheck(age)){
        printf("You are 18 years or older\n");
    }
    else{
        printf("You are not 18 years old\n");
    }

    return 0;
}