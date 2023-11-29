package solutions;

import java.util.Scanner;

public class Main27433 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N;
		N = sc.nextInt();
		
		if (N == 0) {
			System.out.println(1);
		}
		
		else {
			System.out.println(Factorial(N));
		}
		
		sc.close();
		
	}
	
	public static long Factorial(int n) {
		if (n == 1){
			return 1;
		}
		else {
			return n * Factorial(n - 1);
		}
        
    }

}
