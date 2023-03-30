import java.io.*;
import java.util.*;

public class 조합0의개수_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long cnt2 = count2(n) - count2(m) - count2(n - m);
        long cnt5 = count5(n) - count5(m) - count5(n - m);
        System.out.println(Math.min(cnt2, cnt5));
    }

    private static long count2(int n) {
        long count = 0;
        if (n < 2) {
            return 0;
        }
        for (long i = 2; i <= n; i *= 2) {
            count += n / i;
        }
        return count;
    }

    private static long count5(int n) {
        long count = 0;
        if (n < 5) {
            return 0;
        }
        for (long i = 5; i <= n; i *= 5) {
            count += n / i;
        }
        return count;
    }
}
