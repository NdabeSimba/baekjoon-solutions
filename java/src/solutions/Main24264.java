package solutions;

import java.util.Scanner;

public class Main24264 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        // 1 ≤ num ≤ 500,000

        System.out.println(num*num);
        System.out.println(2);
        // double loop means time complexity of O(n^2), leading coefficient of polynomial 2.

        sc.close();
    }
}
