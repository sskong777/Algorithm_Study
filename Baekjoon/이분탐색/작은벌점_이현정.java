import java.util.*;
import java.io.*;

public class 작은벌점_이현정 {
	static int res = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {
	System.setIn(new FileInputStream("src/input.txt"));
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	// 벌점이 최소가 되기 위해서는
	// 두 점수의 격차가 작아야함
	// 1. 정렬
	// 2. 격차가 작은 두 값 구학
	// 3. 반복해서 격차 작은 값 구하기
	StringTokenizer stk  = new StringTokenizer(br.readLine());
	
	int A = Integer.parseInt(stk.nextToken());
	int B = Integer.parseInt(stk.nextToken());
	int C = Integer.parseInt(stk.nextToken());
	
	int[] a = new int[A];
	int[] b = new int[B];
	int[] c = new int[C];
	
	StringTokenizer stk1 = new StringTokenizer(br.readLine());
	for(int j = 0; j < A; j++) {
		a[j] = Integer.parseInt(stk1.nextToken());
	}
	Arrays.sort(a);
		
	StringTokenizer stk2 = new StringTokenizer(br.readLine());
	for(int k = 0; k < B; k++ ) {
		b[k] = Integer.parseInt(stk2.nextToken());
	}
	Arrays.sort(b);
	
	StringTokenizer stk3 = new StringTokenizer(br.readLine());
	for(int l = 0; l < C; l++) {
		c[l] = Integer.parseInt(stk3.nextToken());
	}
	Arrays.sort(c);
	
	// a의 선택에 따라 b, c가 달라짐
	for(int i = 0; i < a.length; i++) {
		int selA = a[i];
		int selB = check(selA, b); // a와 b비교
		
		// c는 이미 정해진 a, b 중 더 격차가 작은 것을 선택해야함
		int selC1 = check(selA, c); // a와 c비교
		int selC2 = check(selB, c); // b와 c비교
		
		// a와 b, a와 c1 비교에서의 최대, 최소 구하기
		int max1 = Math.max(Math.max(selA, selB), selC1);
		int min1 = Math.min(Math.min(selA, selB), selC1);
		int score1 = max1 - min1;
		
		// a와 b, b와 c2 비교에서의 최대, 최소 구하기
		int max2 = Math.max(Math.max(selA, selB), selC2);
		int min2 = Math.min(Math.min(selA, selB), selC2);
		int score2 = max2 - min2;
		
		res = Math.min(res, Math.min(score1, score2));
		
	}
	
	System.out.println(res);
	
	}
	
	// target이 들어있는 범위를 찾는 함수
	// 범위를 찾아야 그 범위에서 가장 유사한 값을 찾을 수 있음
	public static int check(int target, int[] arr) {
		int start = 0;
		int end = arr.length - 1;
		int mid = (start + end) /2;
		int near = arr[mid];
		
		while(start <= end) {
			mid = (start + end)/2;
			
			// 현재 선택한 a와 입력받은 배열에서 같은 값이 있다면
			// 최솟값은 0이므로 선택
			if(arr[mid] == target) {
				return target;
			}
			
			// 입력 받은 배열의 중간 값이 현재 선택한 a보다 작다면
			// a가 뒤영역에 있으니
			// 뒷범위를 선택해서 target과 유사한 값을 찾음
			if(arr[mid] < target) {
				start = mid + 1;
			}
			
			// 입력받은 배열의 중간 값이 현재 선택한 a보다 크다면
			// a가 앞 영역에 있으니
			// 앞범위를 선택해서 target과 유사한 값을 찾음
			else if(arr[mid] > target) {
				end = mid - 1;
			}
			// 현재 범위에서의 중앙값, 현재 선택된 값(초기값:처음 중앙값), 선택된 a
			// 현잭 값보다 새로 들어온 범위의 중앙값이 더 작다면
			// 선택값을 갱신해주어야 함
			if(moreApporix(arr[mid], near, target)) {
				near = arr[mid];
			}
		}
		
		return near;
	}
	
	// 현재 범위에서의 중앙값, 처음 중앙값, 선택된 a
	public static boolean moreApporix(int midCnt, int near, int target) {
		if(Math.abs(midCnt-target) < Math.abs(near - target)) {
			return true;
		}
		return false;
	}
	
}                                                                   