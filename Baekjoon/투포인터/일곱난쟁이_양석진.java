import java.util.*;
import java.io.*;

public class 일곱난쟁이_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[9];

        int sum = 0;
        for (int x = 0; x < 9; x++) {
            arr[x] = Integer.parseInt(br.readLine());
            sum += arr[x];
        }

        for (int x = 0; x < 8; x++) {
            for (int y = x + 1; y < 9; y++) {
                if (sum - arr[x] - arr[y] == 100) {
                    arr[x] = 0;
                    arr[y] = 0;
                    Arrays.sort(arr);
                    for (int z = 2; z < 9; z++) {
                        System.out.println(arr[z]);
                    }
                    return;
                }
            }
        }
    }
}