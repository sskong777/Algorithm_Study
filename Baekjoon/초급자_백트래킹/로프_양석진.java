import java.util.*;
import java.io.*;

public class 로프_양석진 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] rope = new int[N];

        for (int i = 0; i < N; i++) {
            rope[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(rope);

        int max = Integer.MIN_VALUE;

        for (int i = 0; i < N; i++) {
            max = Math.max(max, rope[i] * (N - i));
        }

        System.out.println(max);
    }
}