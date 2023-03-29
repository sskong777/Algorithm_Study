import java.io.IOException;
import java.util.*;

public class 소수찾기_양석진 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int count = 0;

        for (int i = 0; i < N; i++) {
            int input = sc.nextInt();
            boolean isPrime = true;
            if (input == 1) {
                continue;
            }
            for (int x = 2; x <= Math.sqrt(input); x++) {
                if (input % x == 0) {
                    isPrime = false;
                }
            }
            if (isPrime) {
                count++;
            }
        }
        System.out.println(count);
    }
}
