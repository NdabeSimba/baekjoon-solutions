package mathematics;

import java.util.Scanner;

public class Main24265 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        // 1 ≤ n ≤ 500,000

        System.out.println(n*(n-1)/2);
        System.out.println(2); 

        // double loop means time complexity of O(n^2), leading coefficient of polynomial 2.
        // i [1, n-1], j [i+1, n]
        // sum (k=1)^(n-1) k = 1/2 (n-1) n, sum of arithmetic sequences

        sc.close();
    }
}

