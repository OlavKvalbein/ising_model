#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define SIZE 500
#define STEPS (SIZE*SIZE*100)

double T = 1.5; // temperature * k / epsilon
char spin[SIZE][SIZE];

char energyDiff(int i, int j)
{
    char top = spin[(i-1)%SIZE][j];
    char bottom = spin[(i+1)%SIZE][j];
    char left = spin[i][(j-1)%SIZE];
    char right = spin[i][(j+1)%SIZE];

    return 2*spin[i][j]*(top+bottom+left+right);
}

double rand01()
{
    return (double)rand() / RAND_MAX;
}

void step()
{
    int i = (int) (rand01() * SIZE);
    int j = (int) (rand01() * SIZE);
    
    double deltaE = energyDiff(i,j);
    if (deltaE <= 0) {
        spin[i][j] *= -1;
    } else {
        double flip_probability = exp(-deltaE/T);
        if (rand01() < flip_probability)
            spin[i][j] *= -1; 
    }
}

void initialize()
{
    srand(time(NULL));
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            spin[i][j] = rand01() < 0.5 ? -1 : 1;
        }
    }
}

void export()
{
    FILE* fp = fopen("data.csv", "w");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            fprintf(fp, "%d,", spin[i][j] > 0 ? 1 : 0);
        }
        fprintf(fp, "\n");
    }
}

int main() 
{
    printf("simulating...\n");
    initialize();
    for (int i = 0; i < STEPS; i++)
        step();
    printf("exporting...\n");
    export();
    printf("done!\n");
}