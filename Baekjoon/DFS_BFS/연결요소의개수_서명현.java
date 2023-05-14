import java.io.*;
import java.util.*;

public class 연결요소의개수_서명현 {

    static int n;
    static int[][] map;
    static boolean visited[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        map = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            map[x][y] = 1;
            map[y][x] = 1;
        }
        int result = 0;
        for (int i = 1; i < n + 1; i++) {
            if (!visited[i]) {
                dfs(i);
                result++;
            }
        }
        System.out.println(result);
    }

    static void dfs(int x) {
        visited[x] = true;
        for (int i = 1; i < n + 1; i++) {
            if (map[x][i] == 1 && !visited[i]) {
                dfs(i);
                visited[i] = true;
            }
        }
    }
}
