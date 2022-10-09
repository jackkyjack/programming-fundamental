#include<stdio.h>
#include<string.h>
int main(){
    char a[999999];
    scanf("%s[^\n]",a);
    for(int i = strlen(a) ; i >= 0  ; i--) printf("%c",a[i]) ;
    return 0;
} 

//59