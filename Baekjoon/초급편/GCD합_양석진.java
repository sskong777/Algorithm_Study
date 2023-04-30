import java.util.Scanner;

public class GCD합_양석진 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int tc = 0; tc < t; tc++) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            long sum = 0;
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    if (i != j) {
                        sum += GCD(arr[i], arr[j]);
                    }
                }
            }
            System.out.println(sum);
        }
    }
    public static int GCD(int a, int b) {
        if (b == 0) return a;
        return GCD(b, a % b);
    }
}