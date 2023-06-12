import java.util.Scanner;

public class 노땡스_박주원 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		int sum = 0;
		int min = arr[0];
		
		if(n == 1) {
			System.out.println(arr[0]);
		}
		for(int i = 0; i < arr.length - 1; i++) {
			if(arr[i] - arr[i + 1] == -1) {
				continue;
			}else {
				sum += min;
				min = arr[i + 1];
			}
		}
		
		if(arr[arr.length - 2] - arr[arr.length - 1] != -1) {
			sum += arr[arr.length - 1];
		}else {
			sum += min;
		}
		System.out.println(sum);
	}
}
