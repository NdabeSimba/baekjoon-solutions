package solutions;

import java.util.Scanner;

public class Main24313 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int fna1 = sc.nextInt();
        int fna0 = sc.nextInt();
        int c = sc.nextInt();
        int n0 = sc.nextInt();

        if (fna1 * n0 + fna0 <= c * n0 && c >= fna1) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        sc.close();
    }
}

// O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
// f(n) = a1n + a0, g(n) = n
// 0 ≤ |ai| ≤ 100

// if a0 < 0, algorithm don't work. ex) 7n - 3 <= 4n, 7n - 2 <= 5n, 7n - 2 <= 6n
// ...
// new conditional statement needed, c >= a1