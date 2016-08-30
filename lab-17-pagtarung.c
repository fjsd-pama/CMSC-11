#include <stdio.h>

int is_sorted(float nums_list[], int length){
    for (int i = 0; i < length; i++){
        for (int j = 1; j < length; j++){
            if (nums_list[i] < nums_list[j]){
                return 1;
            } else if (nums_list[i] > nums_list[j]){
                return 0;
            }
        }
    }
    return 0;
}



int max(int a, int b){
    if (a > b){
        return a;
    } else{
        return b;
    }
}

int min(int a, int b){
    if (a < b){
        return a;
    } else{
        return b;
    }
}

int LCM(int a, int b){
    for (int i = 1; i < (max (a, b)); i ++){
        if ((min (a, b) * i) % max(a, b) == 0){
            return (min(a, b) * i);
        }
    }
    return (a * b);
}


char toLower(char letter) {
  if ('A' <= letter && letter <= 'Z') {
    // return letter - ('a' - 'A');
    return letter + 32;
  } else {
    return letter;
  }
}

int equals_ignore_case(char arr1[], int length_arr1, char arr2[], int length_arr2){
    int sth = 0;
    
    if (length_arr1 != length_arr2){
        return sth;
    }

    for (int i = 0; i < (length_arr2 + 1); i++){
        sth = (toLower(arr1[i]) == toLower(arr2[i]));
        if (sth == 0){
            return 0;
        }
    }
    
    return sth;
}

float approximate_PI(int n){
    float sum = 0;
    for (int i = 1; i <= n; i += 4){
        sum = sum + (4.0 / i);
    }


    for (int i = 3; i <= n; i += 4){
        sum = sum - (4.0 / i);
    }
    return sum;
}

void modify(int array_given[], int length, int index, int new_val){
    int prev = array_given[index];
    array_given[index] = new_val;
    for (int i = (index + 1); i < length; i++){
        int sth = array_given[i];
        array_given[i] = prev;
        prev = sth;
    }
}

void printArray(int arr[], int length) {
  for (int i = 0; i < length; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}



int main(){
    float list_1[5] = {1, 2, 3, 4, 5};
    float list_2[5] = {2, 2, 3, 4, 5};
    float list_3[5] = {2, 2, 1, 4, 3};
    float list_4[5] = {2, 2, 2, 2, 2};
    float list_5[4] = {4, 2, 3, 4};
    float list_6[4] = {1, 8, 3, 5};    
    float list_7[4] = {3, 0, 4, 3};
    printf("1 == %d\n", is_sorted(list_1, 5));
    printf("1 == %d\n", is_sorted(list_2, 5));
    printf("0 == %d\n", is_sorted(list_3, 5));
    printf("1 == %d\n", is_sorted(list_4, 5));
    printf("0 == %d\n", is_sorted(list_5, 4));
    printf("0 == %d\n", is_sorted(list_6, 4));
    printf("0 == %d\n", is_sorted(list_7, 4));
    printf("2 == %d\n", LCM(2, 1));
    printf("4 == %d\n", LCM(4, 2));
    printf("5 == %d\n", LCM(5, 5));
    printf("0 == %d\n", LCM(9, 0));
    printf("72 == %d\n", LCM(72, 8));
    printf("12 == %d\n", LCM(4, 6));
    char list1[3] = {'a', 'B', 'c'};
    char list2[3] = {'A', 'C', 'c'};
    char list3[3] = {'a', 'B', 'c'};
    char list4[2] = {'a', 'B'};
    char list5[3] = {'X', 'b', 'z'};
    printf("0 == %d\n", equals_ignore_case(list1, 3, list2, 3));
    printf("0 == %d\n", equals_ignore_case(list3, 3, list4, 2));
    printf("0 == %d\n", equals_ignore_case(list3, 3, list5, 3));
    printf("%f\n", approximate_PI(1));
    printf("%f\n", approximate_PI(4));
    printf("%f\n", approximate_PI(9));
    int arr_1[4] = {1, 2, 3, 4};
    modify(arr_1, 4, 0, 4);
    printArray(arr_1, 4);
    return 0;
}