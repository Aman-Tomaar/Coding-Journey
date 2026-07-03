#include <stdio.h>

typedef int num;
typedef char string[50];

num main(){
    num x = 3;
    num y = 4;
    num z = x + y;
    printf("%d\n",z);

    string name = "STRANGE";
    printf("%s\n", name);
    return 0;
}