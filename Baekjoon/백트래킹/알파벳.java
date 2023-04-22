import java.util.*;
import java.io.*;

public class Main {
	static int R, C;
	static int[][] arr;
	// 인덱스 = 방문한 칸의 알파벳
	static boolean[] visited  = new boolean[26];
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int res = 0;
	
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stk = new StringTokenizer(br.readLine());
		R = Integer.parseInt(stk.nextToken());
		C = Integer.parseInt(stk.nextToken());
		arr = new int[R][C];
		
		for(int i = 0; i < R; i++) {
			String st = br.readLine();
			for(int j = 0; j < C; j++) {
				arr[i][j] = st.charAt(j) - 'A';
			}
		}
		
		// 출발 x,  출발 y, 방문 횟수
		dfs(0, 0, 0);
		
		System.out.println(res);
}
	
	public static void dfs(int x, int y, int cnt) {
		//  종료조건: 이미 방문한 칸
		if(visited[arr[x][y]]) {
			res = Math.max(res, cnt);
			return;
		}
		
		else {
			// 아직 방문하지 않은 칸이면, 방문처리
			visited[arr[x][y]] = true;
			// 탐색할 다음 칸 선택
			for(int i = 0; i < 4; i++) {
				int dr = x + dx[i];
				int dc = y + dy[i];
				
				if(dr >= 0 && dc >= 0 && dr < R && dc < C) {
					dfs(dr, dc, cnt + 1);
				}
			}
			
			visited[arr[x][y]] = false;
		}
	}
	
}                                                            