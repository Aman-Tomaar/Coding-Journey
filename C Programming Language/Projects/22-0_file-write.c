#include <stdio.h>

typedef char SA[500];

int main(){

    FILE *pfile1 = fopen("C:\\Office\\temp1.txt", "w");
    FILE *pfile2 = fopen("temp2.txt", "w");


    if(pfile1 == NULL){
        printf("ERROR");
        return 1;
    }
    if(pfile2 == NULL){
        printf("ERROR");
        return 1;
    }

    SA sa1 = "HI MY NAME IS AMAN TOMAR.\nWHAT IS YOUR NAME?\nTHIS JUST A TEST FILE\nTHIS FILE IS IN Office Folder" ;
    SA sa2 = "HI MY NAME IS AMAN TOMAR.\nWHAT IS YOUR NAME?\nTHIS JUST A TEST FILE\nHIS FILE IS IN THE SAME Folder" ;

    fprintf(pfile1, "%s", sa1);
    printf("pfile1 printed successfully!!\n");
    fprintf(pfile2, "%s", sa2);
    printf("pfile2 printed successfully!!\n");

    fclose(pfile1);
    fclose(pfile2);

    return 0;
}