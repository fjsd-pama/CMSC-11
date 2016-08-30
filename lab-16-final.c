#include <stdio.h>
#include <math.h>

int is_teenager(int age){
    return ((age >= 13) && (age <= 19));
}


int is_vowel(char letter){
	return ((letter == 'a') || (letter == 'e') || (letter == 'i') || (letter == 'o') || (letter == 'u'));
}


int Signal_No(int storm_lvl){
	if ((storm_lvl >= 30) && (storm_lvl < 60)){
		return 1;
	}else if ((storm_lvl >= 60) && (storm_lvl < 100)){
		return 2;
	}else if ((storm_lvl >= 100) && (storm_lvl < 185)){
		return 3;
	}else if (storm_lvl >= 185){
		return 4;
	} else{
		return 0;
	}
}

char bump_up(char letter){
	if (letter == 'C'){
		return 'B';
	}else{
		return 'A';
	}
}


#define BMI_CONSTANT 22.0
#define AGE_CONSTANT 45

int risk_level(int BMI, int age){
	if ((BMI >= BMI_CONSTANT) && (age >= AGE_CONSTANT)){
		return 3;
	}else if (((BMI >= BMI_CONSTANT) && (age < AGE_CONSTANT)) || ((BMI < BMI_CONSTANT) && (age >= AGE_CONSTANT))){
		return 2;
    }else{
		return 1;
	}
}


#define PASSING_GRADE 60
#define FE_TOTAL_PT 150.0
#define PERFECT_CLASS_STANDING 100.0
#define FINAL_EXAM_CREDIT 20
#define CLASS_STANDING_CREDIT 80


	
int FE_percentage(int FE_score){
    return ((FE_score / FE_TOTAL_PT) * FINAL_EXAM_CREDIT);
}



int class_standing_percentage(int class_standing){
    return ((class_standing / PERFECT_CLASS_STANDING) * CLASS_STANDING_CREDIT);
}

int is_passing(int class_standing, int FE_score){
    return ((class_standing_percentage(class_standing)) + (FE_percentage(FE_score)) >= PASSING_GRADE);
}


int main(){
	printf("%d\n", is_teenager(12));
	printf("%d\n", is_teenager(20));
	printf("%d\n", is_teenager(15));
	printf("%d\n", is_vowel('a'));
	printf("%d\n", is_vowel('b'));
	printf("The signal number is %d.\n", Signal_No(30));
	printf("The signal number is %d.\n", Signal_No(60));
	printf("The signal number is %d.\n", Signal_No(100));
	printf("The signal number is %d.\n", Signal_No(185));
	printf("%c\n", bump_up('A'));
	printf("%c\n", bump_up('B'));
	printf("%c\n", bump_up('C'));
	printf("Your risk level is %d.\n", risk_level(21, 44)); //low
	printf("Your risk level is %d.\n", risk_level(21, 45)); //medium
    printf("Your risk level is %d.\n", risk_level(22, 44)); //medium
    printf("Your risk level is %d.\n", risk_level(22, 45)); //high
    printf("Your chance of passing is %d.\n", is_passing(80, 0)); //1
    printf("Your chance of passing is %d.\n", is_passing(0, 20)); //0
    printf("Your chance of passing is %d.\n", is_passing(100, 150)); //1
    printf("Your chance of passing is %d.\n", is_passing(0, 0)); //0
}


