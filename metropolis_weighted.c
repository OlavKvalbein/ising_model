#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define SIZE 200
#define STEPS (SIZE*SIZE*100)

double T = 1.0; // temperature * k / epsilon
char spin[SIZE][SIZE];
double J[SIZE][SIZE][4]; // interaction strength for the neighbors top, bottom, left, right.

char energyDiff(int i, int j)
{
    double* Jij = J[i][j];
    char top = Jij[0]*spin[(i-1)%SIZE][j];
    char bottom = Jij[1]*spin[(i+1)%SIZE][j];
    char left = Jij[2]*spin[i][(j-1)%SIZE];
    char right = Jij[3]*spin[i][(j+1)%SIZE];

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

void setJ()
{
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            double *Jij = J[i][j];
            Jij[0] = 1.0; // top
            Jij[1] = 1.0; // bottom
            Jij[2] = -1.0; // left
            Jij[3] = -1.0; // right
        }
    }

    // // a wall in the middle
    // for (int i = 0; i < SIZE; i++) {
    //     J[i][SIZE/2][3] = 0;
    //     J[i][SIZE/2 + 1][2] = 0;
    // }
}

void initialize()
{
    srand(time(NULL));

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            spin[i][j] = rand01() < 0.5 ? -1 : 1;
        }
    }
    setJ();
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