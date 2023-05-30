import java.io.*;
import java.util.*;

public class 알파벳_서명현 {

    static int row;
    static int col;
    static int[][] map;
    static boolean[] visit = new boolean[26];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        row = Integer.parseInt(st.nextToken());
        col = Integer.parseInt(st.nextToken());
        map = new int[row][col];
        for (int i = 0; i < row; i++) {
            String str = br.readLine();
            for (int j = 0; j < col; j++) {
                map[i][j] = str.charAt(j) - 'A';
            }
        }
        dfs(0, 0, 0);
        System.out.println(result);
    }

    static void dfs(int x, int y, int count) {
        if (visit[map[x][y]]) {
            result = Math.max(result, count);
            return;
        }
        visit[map[x][y]] = true;
        for (int i = 0; i < 4; i++) {
            int cx = x + dx[i];
            int cy = y + dy[i];

            if (cx >= 0 && cy >= 0 && cx < row && cy < col) {
                dfs(cx, cy, count + 1);
            }
        }
        visit[map[x][y]] = false;
    }
}
