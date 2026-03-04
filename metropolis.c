#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define SIZE 300
#define STEPS (SIZE*SIZE*100)

double T = 1.5; // T * k / J
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

// random integer in [0, n-1]
int randn(int n)
{
    return (int) (rand01()*SIZE);
}

void step()
{
    int i = randn(SIZE);
    int j = randn(SIZE);
    
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

void export(char* filepath)
{
    FILE* fp = fopen(filepath, "w");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            fprintf(fp, "%d,", spin[i][j] > 0 ? 1 : 0);
        }
        fprintf(fp, "\n");
    }
}

int main(int argc, char* argv[]) 
{
    printf("simulating...\n");
    initialize();
    for (int i = 0; i < STEPS; i++)
        step();
    printf("exporting...\n");
    char *dataFilepath = argv[1];
    export(dataFilepath);
    printf("done!\n");
}