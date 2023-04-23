import java.util.*;
import java.io.*;

public class 동전0_양석진 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Integer[] arr = new Integer[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int coinCount = 0;
        int price = 0;
        int totalCount = 0;

        Arrays.sort(arr, Collections.reverseOrder());

        for (int x = 0; x < arr.length; x++) {
            if (arr[x] > K) {
                continue;
            }
            coinCount = K / arr[x];
            K -= coinCount * arr[x];
            totalCount += coinCount;
        }

        System.out.println(totalCount);
    }
}