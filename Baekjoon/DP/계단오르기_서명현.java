import java.io.*;

public class 계단오르기_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[301];
        int[] dp = new int[301];
        for (int i = 1; i <= n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        dp[1] = stairs[1];
        dp[2] = stairs[1] + stairs[2];
        dp[3] = Math.max(stairs[1] + stairs[3], stairs[2] + stairs[3]);

        for (int i = 4; i <= n; i++) {
            dp[i] = stairs[i] + Math.max(dp[i - 2], stairs[i - 1] + dp[i - 3]);
        }
        System.out.println(dp[n]);
    }
}
