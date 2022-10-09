#include<stdio.h>
#include<string.h>
int main(){

    char a[999999];
    int i;
    scanf("%s[^\n]",a);
    i=strlen(a);
    while(1){
    if(i>=0){
        printf("%c",a[i]);
        i--;
    }
    if(i<0){
        break;
    }
    }
    return 0 ;

}