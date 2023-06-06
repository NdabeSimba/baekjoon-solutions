package solutions;

import java.util.Scanner;

public class Main1157 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine().toUpperCase();

		int[] count = new int[26];

		for (int i = 0; i < word.length(); i++) {
			int num = word.charAt(i) - 'A';
			count[num]++;
		}

		int wordCount = 0;
		char answer = '?';

		for (int i = 0; i < count.length; i++) {

			if (wordCount < count[i]) {

				wordCount = count[i];
				answer = (char) (i + 'A');

			} else if (wordCount == count[i]) {
				answer = '?';
			}
		}
		System.out.println(answer);
		sc.close();
	}
}
