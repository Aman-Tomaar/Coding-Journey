#include <stdio.h>

void birthday(int *age);

int main(){

    int age =19;

    birthday(&age);
    printf("%d\n",age);


    return 0;
}
void birthday(int *age){
    (*age)++;
}