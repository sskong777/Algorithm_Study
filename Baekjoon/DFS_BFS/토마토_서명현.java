import java.io.*;
import java.util.*;

public class 토마토_서명현 {

    static int n;
    static int m;
    static int[][] map;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};
    static Queue<int[]> queue = new LinkedList<>();
    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    queue.add(new int[]{i, j});
                }
            }
        }
        bfs();
        System.out.println(result);
    }

    static void bfs() {
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            int x = p[0];
            int y = p[1];
            for (int i = 0; i < dx.length; i++) {
                int nextX = x + dx[i];
                int nextY = y + dy[i];
                if (checkValidation(nextX, nextY) && map[nextX][nextY] == 0) {
                    map[nextX][nextY] = map[x][y] + 1;
                    queue.add(new int[]{nextX, nextY});
                }
            }
        }
        if (checkAnyZero()) {
            result = -1;
            return;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result = Math.max(map[i][j] - 1, result);
            }
        }
    }

    static boolean checkValidation(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    static boolean checkAnyZero() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    return true;
                }
            }
        }
        return false;
    }
}
