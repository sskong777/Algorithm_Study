import java.util.Scanner;

public class 첨탑밀어서부수기_박주원 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] h = new int[n];
		int cnt = 0;

		for (int i = 0; i < n; i++) {
			h[i] = sc.nextInt();
		}

		for (int i = 0; i < n - 1; i++) {
			while (i < n && h[i] > h[i + 1]) {
				i++;
				cnt++;
			}

		}
		System.out.println(cnt);
	}
}