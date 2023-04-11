import java.io.*;
import java.util.*;

public class ThreeDots_서명현 {

    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            int m = Integer.parseInt(br.readLine());
            arr = new int[m];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            int result = 0;
            Arrays.sort(arr);
            for (int i = 0; i < m - 2; i++) {
                for (int j = i + 2; j < m; j++) {
                    if ((arr[i] + arr[j]) % 2 == 0) {
                        int mid = (arr[i] + arr[j]) / 2;
                        if (binarySearch(i, j, mid)) {
                            result++;
                        }
                    }
                }
            }
            System.out.println(result);
        }
    }

    private static boolean binarySearch(int start, int end, int key) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (key == arr[mid]) {
                return true;
            } else if (key < arr[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }
}
