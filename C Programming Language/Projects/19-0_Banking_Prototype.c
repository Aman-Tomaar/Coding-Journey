#include <stdio.h>

void checkbalance(float balance);
float deposit();
float withdraw(float balance);

int main(){

    int choice = 0;
    float balance = 0.0f;

    printf("**** WELCOME TO THE WORLD BANK ****\n");
    do{
        printf("What do you wanna do \n1.Check Balance \n2.Deposit \n3.Withdraw \n4.EXIT \nEnter your choice: ");
        scanf("%d",&choice);

        printf("X--------------------------------X\n");

        if(choice < 1 || choice > 4){
            printf("INVALID CHOICE!!\n");
        }

        switch(choice){
            case 1:
                checkbalance(balance);
                break;
            case 2:
                balance += deposit();
                break;    
            case 3:
                balance -= withdraw(balance);
                break;
            case 4:
                printf("Thank you for visiting! Processing exit...\n");
                break;
            
        }
        printf("X--------------------------------X\n");

    }while(choice != 4);

    printf("**** THANK YOU FOR VISITING!! ****");
    

    return 0;
}


void checkbalance(float balance){
    printf("YOUR BALANCE IS : $%.2f\n",balance);
}
float deposit(){
    float dmoney = 0.0f;
    printf("ENTER THE AMOUNT OF MONEY YOU WANT TO DEPOSIT: ");
    scanf("%f", &dmoney);
    printf("DEPOSITING $%.2f IN YOUR BANK ACCOUNT\n",dmoney);
    printf("$%.2f MONEY DEPOSITED SUCCESSFULLY\n",dmoney);
    return dmoney;
}
float withdraw(float balance){
    float wmoney = 0.0f;
    printf("ENTER THE AMOUNT OF MONEY YOU WANT TO WITHDRAW: ");
    scanf("%f", &wmoney);
    printf("WITHDRAWING $%.f FROM YOUR BANK ACCOUNT\n",wmoney);
    if(balance < wmoney){
        printf("WITHDRAWING FAILED !!!\nYOU ONLY GOT $%.2f IN YOUR BANK ACCOUNT\n",balance);
        return 0.0f;
    }
    else{
        printf("$%.2f MONEY WITHDRAWL SUCCESSFULLY\n",wmoney);
        return wmoney;
    }
}
