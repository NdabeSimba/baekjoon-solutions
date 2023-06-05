package bruteforcing;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main2798 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] numArray = new int[N];

        st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < N; i++) {
            numArray[i] = Integer.parseInt(st.nextToken());
        }

        int result = search(numArray, N, M);
        System.out.println(result);

    }

    static int search(int[] numArray, int N, int M) {
        int result = 0;

        for (int i = 0; i < N - 2; i++) {

            for (int j = i + 1; j < N - 1; j++) {

                for (int k = j + 1; k < N; k++) {

                    int numSum = numArray[i] + numArray[j] + numArray[k];

                    if (M == numSum) {
                        return numSum;
                    }

                    if (result < numSum && numSum < M) {
                        result = numSum;
                    }

                }

            }

        }
        return result;
    }

}
