//9th november 2015
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

unsigned long long play(){
    unsigned long long sum = 2;
    int toss = rand() % 2;
    while(toss){
        if (sum > 9223372036854775800){
            printf("Error: Computed value too high!");
            exit(1);
        }
        sum*=2;
        toss = rand() % 2;
    }
    return sum;
    
}


int main(){
    srand(time(NULL));
    unsigned long long plays = 1000000000;
    unsigned long long sum,i,n=1;
    while(n<plays){
        sum=0;
        n*=2;
        for (i=0; i < n; i++){
            if (sum > 9223372036854775800){
                printf("Error: Computed value too high!");
                exit(1);
            }
            sum+=play();
        }
        unsigned long long average = sum / n;
        printf("played %llu times, mean outcome %llu\n",n,average);
    }
}