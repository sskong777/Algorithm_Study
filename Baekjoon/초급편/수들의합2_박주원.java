import java.util.Scanner;

public class 수들의합2_박주원 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		int start = 0, end = 0, count = 0, sum = 0;
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		while(start < N) {
			if(sum > M || end == N) {
				sum = arr[start++];
			}
			else {
				sum += arr[end++];
			}
			if(sum == M) {
				count++;
			}
			System.out.println(count);
		}
	}

}
