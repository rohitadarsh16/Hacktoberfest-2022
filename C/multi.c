#include <stdio.h>
int main() {    

    int number1, number2, mult;
    
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    
    mult = number1 * number2;      
    
    printf("%d X %d = %d", number1, number2, mult);
    return 0;
}
