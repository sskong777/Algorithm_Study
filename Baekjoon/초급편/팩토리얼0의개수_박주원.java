import java.util.Scanner;

public class 팩토리얼0의개수_박주원 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int cnt = 0;
		
		while(num >= 5) {
			cnt += num / 5;
			num /= 5;
		}
		System.out.println(cnt);
	}

}
