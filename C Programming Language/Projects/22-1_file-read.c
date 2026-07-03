#include <stdio.h>

int main(){

    FILE *pfile = fopen("temp2.txt","r");

    char buffer[1024] = {0};

    if(pfile == NULL){
        printf("ERROR");
        return 1;
    }

    while(fgets(buffer, sizeof(buffer), pfile) != 0){
        printf("%s",buffer);
    }

    fclose(pfile);

    return 0;
}