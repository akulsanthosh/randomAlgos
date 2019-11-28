#include <stdio.h>
int main(){
    char a[20];
    int trans[5][2] = {1,2,3,2,1,4,3,2,1,4};
    int state=0;
    printf("Enter the string : ");
    scanf("%s",a);
    for(int i=0;a[i]!='\0';i++){
        state=trans[state][a[i]-'0'];
    }
    if(state==3||state==4)
        printf("Valid\n");
    else
        printf("invalid\n");  
}