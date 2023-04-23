import java.io.*;
import java.util.*;

public class 차이를최대로_서명현 {

    static int n;
    static int[] arr;
    static int[] arr2;
    static boolean[] visited;
    static int sum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        arr2 = new int[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        dfs(0);
        System.out.println(sum);
    }

    private static void dfs(int count) {
        if (count == n) {
            int temp = 0;
            for (int i = 0; i < n - 1; i++) {
                temp += Math.abs(arr2[i] - arr2[i + 1]);
            }
            sum = Math.max(sum, temp);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                arr2[count] = arr[i];
                visited[i] = true;
                dfs(count + 1);
                visited[i] = false;
            }
        }
    }
}
