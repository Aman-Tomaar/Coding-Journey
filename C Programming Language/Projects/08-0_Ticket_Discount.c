#include <stdio.h>
#include <stdbool.h>

int main(){

    float tic = 10.00;
    bool student = false; // Using false/true is clearer than 0/1
    bool senior = true;

    if(student){
        if(senior){
            // Student AND Senior discount (30% off)
            tic *= 0.7; 
            printf("Student Senior Discount: $%.2f\n", tic);
        }
        else{
            // Just Student discount (10% off)
            tic *= 0.9; 
            printf("Student Discount: $%.2f\n", tic);
        }
    }
    else if(senior){
        // Just Senior discount (20% off)
        tic *= 0.8; 
        printf("Senior Discount: $%.2f\n", tic);
    }
    else{
        printf("NO DISCOUNT: $%.2f\n", tic);
    }

    return 0;
}