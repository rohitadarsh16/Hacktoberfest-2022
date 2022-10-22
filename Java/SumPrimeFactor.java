import java.util.*;

public class SumPrimeFactor {

	public static boolean isPrime(int n) {
		for (int i = 2; i < n; i++) {
			if (n % i == 0)
				return false;
		}
		return true;
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int x, s = 0;
		System.out.println("Enter a no. : ");
		x = sc.nextInt();
		for (int i = 2; i <= x; i++) {
			if (isPrime(i)) {
				if (x % i == 0)
					s += i;
			}
		}
		System.out.println("Sum of Prime factors of "+x+" = "+s);
	}
}
