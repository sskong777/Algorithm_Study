import java.io.*;
import java.util.*;

public class 등차수열과쿼리_서명현 {

    static int a;
    static int d;
    static int gcd;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(br.readLine());
        gcd = gcd(a, d);

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            sb.append(sumOrGcd(type, l, r)).append("\n");
        }
        System.out.println(sb);
    }

    private static long sumOrGcd(int type, long l, long r) {
        if (type == 1) {
            return (r - l + 1) * (2 * a + (r + l - 2) * d) / 2;
        }
        return l == r ? a + (l - 1) * d : gcd;
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
