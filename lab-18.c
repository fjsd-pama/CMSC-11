#include <stdio.h>

int str_length(char string[]){
	int len = 0;
	for (int i = 0; string[i] != '\0'; i++){
		len += 1;    
	}
	return len;
}

// void str_copy(char source_str[], char dest[]){
//      char dest[] = source_str;
// }

void str_copy(char strA[], char strB[]){
	for (int i = 0; i < (str_length(strB)); i ++){
		strB[i] = strA[i];
	}	
}

void printArray(char arr[], int length) {
  for (int i = 0; i < length; i++) {
    printf("%c ", arr[i]);
  }
  printf("\n");
}

// int str_in(char str_A[], char str_B){
// 	for (int i = 0; str_A[i] != '\0'; i++){
// 		for (int i = 0; str_B[i] != '\0'; i ++){

// 		}
// 	}
// }

int str_in(char str_A[], char sub[]) {
	for(int i = 0; str_A[i] != '\0'; i++) {
		int k = 0;
		for(int j = i; str_A[j] != '\0'; j++) {
			if(str_A[j] != sub[k]) {
				break;
			} 
			k++;
			if(sub[k] == '\0') {
				return 1;
			}
		}
	}
	return 0;
}

int main(){
	char str_1[] = "Hello World!";
	printf("%d\n", str_length(str_1));
	char str_2[] = "Hahaha";
	char str_3[] = "Meeee";
	str_copy("Hello", str_3);
	str_copy("Hello", str_2);
	char dest[20];
	str_copy("Hello", dest);
	printf("%s\n", dest);
	printArray(str_3, str_length(str_3));
	printArray(str_2, str_length(str_2));
	printf("%d\n", str_in("Hello World!", "ello"));
	printf("%d\n", str_in("Hello World!", "Hello"));
	printf("%d\n", str_in("Hello World!", "World"));
	return 0;
}
