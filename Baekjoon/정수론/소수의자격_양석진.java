import java.io.*;
import java.io.IOException;
import java.util.*;

public class 소수의자격_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        int answer = 0;
        for (int i = A; i <= B; i++) {
            if (isPrime(i)) {
                int temp = i;
                while (temp != 0) {
                    if (temp % 10 == D) {
                        answer++;
                        break;
                    }
                    temp /= 10;
                }
            }
        }
        System.out.println(answer);
    }
    public static boolean isPrime(int n) {
        if (n == 1) {
            return false;
        }

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
