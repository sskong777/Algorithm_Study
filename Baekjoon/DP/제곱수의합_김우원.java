import java.util.Arrays;
import java.util.Scanner;
/*
[1699] 제곱수의 합
 */
public class 제곱수의합_김우원 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] dp = new int[N+1];
        Arrays.fill(dp, 100000000);
        dp[0] = 0;
        for(int i = 0; i<dp.length; i++) {
            for(int j = 1; i+j*j<dp.length; j++) {
                dp[i+j*j] = Math.min(dp[i+j*j], dp[i]+1);
            }
        }
        System.out.println(dp[N]);
        sc.close();
    }
}
