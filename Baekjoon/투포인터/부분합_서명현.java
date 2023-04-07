import java.io.*;
import java.util.*;

public class 부분합_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int sum = 0;
        int result = 100000;
        while (true) {
            if (sum >= s) {
                sum -= arr[left++];
                result = Math.min(result, right - left + 1);
                continue;
            }
            if (right == n) {
                break;
            }
            sum += arr[right++];
        }
        if (result == 100000) {
            result = 0;
        }
        System.out.println(result);
    }
}
