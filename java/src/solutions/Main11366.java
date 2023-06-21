package solutions;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11366 {
    private static final int[] FIBO = new int[47];
    private static final String NEW_LINE = "\n";

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        makeCoefiicient();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0 && b == 0 && c == 0)
                break;
            sb.append(getOrcCount(a, b, c)).append(NEW_LINE);
        }

        System.out.print(sb);
    }

    private static void makeCoefiicient() {
        FIBO[0] = FIBO[1] = 1;

        for (int i = 2; i < FIBO.length; i++) {
            FIBO[i] = FIBO[i - 1] + FIBO[i - 2];
        }
    }

    private static int getOrcCount(int x, int y, int day) {
        if (day == 1)
            return x + y;
        if (x == 0 && y == 0)
            return 0;

        return x * FIBO[day - 1] + y * FIBO[day];
    }
}
