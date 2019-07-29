#include<stdlib.h>
#include<stdio.h>
#include "division.h"
#include "add.h"

void main()
{
    char ch;

    int a, b;
    printf("Enter the the operation +,-,*,/");
    scanf("%c", &ch);
    
    printf("Enter the 2 numbers");
    scanf("%d,%d", &a, &b);
    
    switch(ch)
    {
            case'+':
                    add(a,b);
                    break;
            case '-':
                    printf("the ans is %d", a-b);
                    break;
            case '*':
                    printf("the ans is %d", a*b);
                    break;
            case '/':
                    divi(a,b);
                    break;
           default:
                   printf("Error in operation");
                   
    }
}
