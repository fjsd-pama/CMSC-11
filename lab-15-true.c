#include <stdio.h>
#include <math.h>

float num1(int p){
	return sqrt(pow(1 - p, 3));
}

float num2(int n){
	return (n * (n - 1)) / 2.0;
}

float num3(int x, int y){
	return sqrt(50 * (pow(x, 3)) * (pow(y,5)));
}

float num4(){
	return (4 * sqrt(5)) + (3 * sqrt(125)) - (sqrt(20));
}

float num5(int x){
	return (x * (x - 1)) / (x * (x + 1));
}

float num6(int r){
	return (4 * M_PI * (pow(r, 2)));
}

float num7(int a, int r){
	return (r * pow((cos(a)), 2)) + (r * pow((sin(a)), 2));
}

float num8(int a, int b, int c, int x){
	return (a * pow((x + (b/ (2 * a))), 2)) - (pow(b, 2) - (4 * a * c)) / (4 * a);
}

float num9(int x){
	return (-2 * pow(x,2)) + x - 1;
}

int num10(int x){
	return x + fabs(x - 2);
}




int main(){
	printf("%f is the result\n", num1(1)); // expect 0.0
	printf("%f is the result\n", num2(1)); // expect 0.0
	printf("%f is the result\n", num3(1, 1)); // expect 7.071068
	printf("%f is the result\n", num4()); // expect 38.013157
	printf("%f is the result\n", num5(1)); // expect 0.0
	printf("%f is the result\n", num6(1)); // expect 12.566371
	printf("%f is the result\n", num7(1, 1)); // expect 1.0
	printf("%f is the result\n", num8(1, 1, 1, 1)); // expect 1.75
	printf("%f is the result\n", num9(1)); // expect -2.0
	printf("%f is the result\n", num10(1)); // expect -2.0
	return 0;
}
