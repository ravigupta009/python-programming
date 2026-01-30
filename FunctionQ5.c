/*Swap two numbers using pass by reference*/
#include <stdio.h>
 void swap(int *a, int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
 }
int main(){
    int x,y;
    printf("enter two numbers x and y =:");
    scanf("%d %d",&x,&y);
    swap(&x,&y);
    printf("%d %d",x,y);
    return 0;
}
