import java.util.Scanner;

public class November_박주원 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		if((a + 7 * b) >= 1 && (a + 7 * b) <= 30) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
	}

}
