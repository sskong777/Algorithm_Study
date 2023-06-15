import java.io.*;
import java.util.*;

/**
 * 미완
 */
public class 스파이_서명현 {

    static int[][] map = new int[3][2];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < 2; i++) {
            st = new StringTokenizer(br.readLine());
            map[0][i] = Integer.parseInt(st.nextToken());
            map[1][i] = Integer.parseInt(st.nextToken());
            map[2][i] = Integer.parseInt(st.nextToken());
        }

        int count = 0;
        int point = 0;
        int place = 0;

        while (count++ < n) {
            Loop:
            for (int i = 0; i < map.length; i++) {
                place = i;
                for (int j = 0; j < map[0].length; j++) {
                    point += map[i][j];
                    if (point >= m) {
                        point = 0;
                        break Loop2;
                    }
                }
            }
            count = 0;
            point = 0;
        }
    }
}
