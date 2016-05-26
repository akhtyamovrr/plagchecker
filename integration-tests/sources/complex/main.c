#include "stdio.h"

/*
Simple or complex number
*/
int main(void) {
	int number = 10;
	int divs = 0; // nubmer of deviders
	int i = 0;
    for (i = 1; i < number; i++)
    {
    	if (number % i == 0)
    		divs++;
    }
    if (divs == 1)
    	printf("simple");
    else
    	printf("complex");
    return 0;
}