import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 등차수열과쿼리_김우원 {//[23888] 등차수열과 쿼리
    static int a, d, gcd;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./APS/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        a = Integer.parseInt(stk.nextToken());
        d = Integer.parseInt(stk.nextToken());
        gcd = getGcd(a, d);
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            stk = new StringTokenizer(br.readLine());
            int q = Integer.parseInt(stk.nextToken());
            int l = Integer.parseInt(stk.nextToken());
            int r = Integer.parseInt(stk.nextToken());
            sb.append(solve(q, l, r)).append("\n");
        }
        System.out.println(sb);
    }

    private static long solve(int q, long l, long r) {
        if (q == 1) {
            return a * (r - l + 1) + d * ((r + l - 2) * (r - l + 1) / 2);
        } else {
            return l == r ? a + (l - 1) * d : gcd;
        }
    }

    private static int getGcd(int a, int b) {
        return b == 0 ? a : getGcd(b, a % b);
    }
}
