#include <stdio.h>
#include <stdlib.h>

int main(){

    int number = 0;
    printf("ENTER THE AMOUT OF PRODUCTS YOU WANNA PRICE: ");
    scanf("%d",&number);

    float *price = malloc(number * sizeof(float)); 
    if(price == NULL){
        printf("ERROR OCCUERED !!!");
        return 1;
    }

    for(int i = 0; i < number; i++){
        printf("ENTER THE PRICE OF #%d PRODUCT: ",i + 1);
        scanf("%f", &price[i]);
    }

    int newn = 0;
    printf("ENTER THE NEW AMOUNT OF PRODUCTS YOU WANNA PRICE: ");
    scanf("%d",&newn);

    float *temp = realloc(price , sizeof(float));

    if(temp == NULL){
        printf("ERROR");
    }
    else{
        price = temp;
        temp = NULL;

        for(int i = number; i < newn; i++){
           printf("ENTER THE PRICE OF #%d PRODUCT: ",i + 1);
           scanf("%f", &price[i]); 
        }
        for(int i = 0; i < newn; i++){
            printf("THE PRICE OF #%d PRODUCT IS $%.2f \n", i + 1, price[i]);
        }
    }

    price = NULL;
    free(price);
    free(temp);
    return 0;
}