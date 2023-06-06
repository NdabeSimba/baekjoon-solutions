package solutions;

import java.util.Scanner;
import java.util.Arrays;

public class Main25206 {
    public static void main(String[] args) {

        String[] grade = { "A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F" };
        double[] score = { 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0 };

        Scanner sc = new Scanner(System.in);

        double creditSum = 0;
        double majorGPA = 0;

        for (int i = 0; i < 20; i++) {

            String listInput = sc.nextLine();
            String list[] = listInput.split(" ");

            if (!list[2].equals("P")) {

                int Index = Arrays.binarySearch(grade, list[2]);

                creditSum += Double.parseDouble(list[1]);
                majorGPA += score[Index] * Double.parseDouble(list[1]);

            }

        }
        System.out.printf("%.6f", majorGPA / creditSum);
        sc.close();
    }

}
