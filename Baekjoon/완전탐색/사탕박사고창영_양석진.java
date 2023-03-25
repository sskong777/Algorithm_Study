import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class 사탕박사고창영_양석진 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- > 0) {
            br.readLine();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            char[][] candy = new char[r][c];
            int cnt = 0;

            // 입력 먼저 받기
            for (int x = 0; x < r; x++) {
                String s = br.readLine();
                for (int y = 0; y < c; y++) {
                    candy[x][y] = s.charAt(y);
                }
            }
            // 가로 사탕 탐색하기
            for (int x = 0; x < r; x++) {
                for (int y = 0; y < c - 2; y++) {
                    if (candy[x][y + 2] == '<' && candy[x][y + 1] == 'o' && candy[x][y] == '>') {
                        cnt++;
                    }
                }
            }
            // 세로 사탕 탐색하기
            for (int x = 0; x < r - 2; x++) {
                for (int y = 0; y < c; y++) {
                    if (candy[x][y] == 'v' && candy[x + 1][y] == 'o' && candy[x + 2][y] == '^') {
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}