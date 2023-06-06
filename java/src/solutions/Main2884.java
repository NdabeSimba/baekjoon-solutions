package solutions;

import java.util.Scanner;

public class Main2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int time = sc.nextInt();
		int min = sc.nextInt();

		if (min < 45) {
			time = (time - 1);
			min = (min + 15);
			if (time < 0) {
				time = 23;
				System.out.println(time + " " + min);
			} else {
				System.out.println(time + " " + min);
			}
		} else {
			System.out.println(time + " " + (min - 45));
		}
		sc.close();
	}
}