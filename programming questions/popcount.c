#include <stdio.h>

int popcount(int v){
	v = v - ((v >> 1) & 0x55555555);                    // reuse input as temporary
	v = (v & 0x33333333) + ((v >> 2) & 0x33333333);     // temp
	int c = ((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24; // count
	return c;
}

int main(void) {
	int v;
    	printf("Please input an integer value: ");
    	scanf("%i", &v); 
	printf("%i", popcount(v));
	return 0;
}
