package solutions;

import java.util.Scanner;

public class Main15727 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        if (num % 5 == 0) {
            System.out.println(num / 5);
        } else {
            System.out.println(num / 5 + 1);
        }

        sc.close();
    }

}
