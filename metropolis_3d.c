#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define SIZE 30
#define STEPS_PER_PIXEL 500

#define STEPS (SIZE*SIZE*SIZE*STEPS_PER_PIXEL)

double T = 1.5; // temperature * k / epsilon
char spin[SIZE][SIZE][SIZE];
// interaction strength for the neighbors. Ordering is 
// top, bottom, left, right, front, back.
double J[SIZE][SIZE][SIZE][6];

char energyDiff(int i, int j, int k)
{
    double* Jijk = J[i][j][k];
    char top = Jijk[0]*spin[(i-1)%SIZE][j][k];
    char bottom = Jijk[1]*spin[(i+1)%SIZE][j][k];
    char left = Jijk[2]*spin[i][(j-1)%SIZE][k];
    char right = Jijk[3]*spin[i][(j+1)%SIZE][k];
    char front = Jijk[3]*spin[i][j][(k-1)%SIZE];
    char back = Jijk[3]*spin[i][j][(k+1)%SIZE];

    return 2*spin[i][j][k]*(top+bottom+left+right+front+back);
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
    int k = randn(SIZE);
    
    double deltaE = energyDiff(i,j,k);
    if (deltaE <= 0) {
        spin[i][j][k] *= -1;
    } else {
        double flip_probability = exp(-deltaE/T);
        if (rand01() < flip_probability)
            spin[i][j][k] *= -1; 
    }
}

void setJ()
{
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            for (int k = 0; k < SIZE; k++) {
                double *Jijk = J[i][j][k];
                Jijk[0] = 1.0; // top
                Jijk[1] = 1.0; // bottom
                Jijk[2] = 1.0; // left
                Jijk[3] = 1.0; // right
                Jijk[4] = 1.0; // front
                Jijk[5] = 1.0; // back
            }
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
            for (int k = 0; k < SIZE; k++) {
                spin[i][j][k] = rand01() < 0.5 ? -1 : 1;   
            }
        }
    }
    setJ();
}

void export()
{
    FILE* fp = fopen("data.txt", "w");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            for (int k = 0; k < SIZE; k++) {
                fputc((spin[i][j][k] > 0 ? '1' : '0'), fp);
            }
        }
    }
    fclose(fp);
}

int main() 
{
    printf("simulating...\n");
    initialize();
    for (int i = 0; i < STEPS; i++) {
        step();
    }
    printf("exporting...\n");
    export();
    printf("done!\n");
}