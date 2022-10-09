import java.util.Scanner;

public class calculator {
      static Scanner scn=new Scanner(System.in);
      
    public static void main(String[] args) {
        char ch;
        do {
            ch = scn.next().charAt(0);  // Use cin in case of c++
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%') {
                operation(ch);
            } else {
                if (ch != 'x' && ch != 'X')
                    System.out.println("Invalid operation. Try again.");
            }
        } while (ch != 'x' && ch != 'X');
    }
    public static void operation(char ch) {
        int a = scn.nextInt(); // Use cin in case of c++
        int b = scn.nextInt(); // Use cin in case of c++
        int res = 0;
        switch (ch) {
        case '+': {
            res = a + b;
            break;
        }
        case '-': {
            res = a - b;
            break;
        }
        case '*': {
            res = a * b;
            break;
        }
        case '/': {
            res = a / b;
            break;
        }
        case '%': {
            res = a % b;
            break;
        }
        }
        System.out.println(res);
    }
    }
