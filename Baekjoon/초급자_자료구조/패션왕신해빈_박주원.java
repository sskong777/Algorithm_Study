import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class 패션왕신해빈_박주원 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int cnt = sc.nextInt();

		for (int i = 0; i < cnt; i++) {
			Map<String, Integer> set = new HashMap<>();
			int n = sc.nextInt();
			for (int j = 0; j < n; j++) {
				String str = sc.next();
				String key = sc.next();
				set.put(key,set.getOrDefault(str, 0) + 1);
			}
			
			int ans = 1;
            for (int val : set.values()) {
            	ans *= val + 1;
            }
                
            System.out.println(ans - 1);
		}
	}
}
