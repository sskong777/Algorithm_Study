import java.util.*;
import java.io.*;

public class 보석상자_이현정 {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(stk.nextToken());
		int M = Integer.parseInt(stk.nextToken());
		
		int[] K = new int[M];
		for(int i = 0; i < M; i++) {
			K[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(K);
		int start = 1;
		int end = K[K.length-1];
		
		int maxCnt = 0;
		int res = 0;
		
		while(start <= end) {
			
			// 나눠줄 사탕
			int mid = (start + end) / 2;
			// 사탕을 받는 학생
			int sum = 0;
			
			// 각 사탕의 개수가 적힌 배열의 탐색
			for(int i = 0; i < M; i++) {
				
				// 시탕을 나눠주는 경우의 수
				if(K[i] % mid == 0) {
					sum += K[i]/mid;
				}
				else {
					sum += K[i]/mid + 1;
				}
			}
			
			// 만약 사탕을 받게된느 학생이 더 많다면
			// 나눠줄 수 없으므로
			// 사탕의 양을 늘려 더 적은 학생들에게 배분될 수 있게 한다
			if(sum > N) {
				start = mid+1;
			}
			
			// 그 반대로, 사탕을 받게되는 학생이 적다면
			// 가능하다, 왜냐면 사탕을 받지 못하는 학생들도 있으므로
			// 하지만, 보석을 줄 수있는 최소 값으 찾아야 하므로 계속 진행
			else {
				end = mid - 1;
				res = mid;
			}
		}
		
		System.out.println(res);
	}
}                                                                   