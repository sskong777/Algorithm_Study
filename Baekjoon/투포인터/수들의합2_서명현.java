import java.io.*;
import java.util.*;

public class 수들의합2_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int result = 0;
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int sum = 0;
        while (left < n) {
            if (sum > m || right == n) {
                sum -= arr[left++];
            } else {
                sum += arr[right++];
            }
            if (sum == m) {
                result++;
            }
        }
        System.out.println(result);
    }
}
