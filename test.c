#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rand01()
{
    return (double)rand() / RAND_MAX;
}

int main()
{
	printf("%d\n", (int)round(0.9));
}