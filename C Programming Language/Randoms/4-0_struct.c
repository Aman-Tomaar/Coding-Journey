#include <stdio.h>
#include <string.h>

typedef struct{
    char name[50];
    int age;
    float marks;
}userinfo;

void uinfo(userinfo user);

int main(){
    userinfo user1 = {"Aman Tomar", 18, 9.9};
    userinfo user2 = {"Aaditya Batra", 19, 8.2};
    userinfo user3 = {"Gargi Gautam", 19, 7.9};

    uinfo(user1);
    uinfo(user2);
    uinfo(user3);

    return 0;
}

void uinfo(userinfo user){
    printf("NAME = %s\nAGE = %d\nMARKS = %.2f\n\n", user.name, user.age, user.marks );
}