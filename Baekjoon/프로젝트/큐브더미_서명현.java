import java.io.*;
import java.util.*;

public class 큐브더미_서명현 {

    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        boolean[][][] visited = new boolean[n + 1][n + 1][n + 1];
        int[][] arr = new int[m][3];

        int count = 0;
        for (int l = 0; l < m; l++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            arr[l] = new int[]{i, j, k};
            visited[i][j][k] = true;
        }

        for (int l = 0; l < m; l++) {
            int i = arr[l][0];
            int j = arr[l][1];
            int k = arr[l][2];
            if (checkValidation(i, j, k)) {
                if (visited[i - 1][j][k] && visited[i + 1][j][k] && visited[i][j - 1][k] && visited[i][j + 1][k] && visited[i][j][k - 1] && visited[i][j][k + 1]) {
                    count++;
                }
            }
        }
        System.out.println(count);
    }
    private static boolean checkValidation(int i, int j, int k) {
        return i > 1 && i < n && j > 1 && j < n && k > 1 && k < n;
    }
}
