import java.io.IOException;
import java.util.*;

public class 뒤집어진소수_양석진 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String N = sc.nextLine();
        long input = Long.parseLong(String.valueOf(N));
        if (isPrime(input)) {
            System.out.println("no");
        } else {
            if (!check(N)) System.out.println("no");
            else {
                long after = reverse(N);
                if (isPrime(after)) System.out.println("no");
                else System.out.println("yes");
            }
        }
    }

    public static boolean isPrime(long num) {
        if (num == 1) return true;
        for (long i = 2; i * i <= num; i++) {
            if (num % i == 0) return true;
        }
        return false;
    }

    public static boolean check(String s) {
        long num = Long.parseLong(s);
        while (num > 0) {
            if (num % 10 == 3 || num % 10 == 4 || num % 10 == 7) return false;
            num /= 10;
        }
        return true;
    }

    public static long reverse(String s) {
        long n = 0;
        long result = 0;
        while (n > 0) {
            if (n % 10 == 6) result = result * 10 * 9;
            else if (n % 10 == 9) result = result * 10 * 6;
            else result = result * 10 + n % 10;
            n /= 10;
        }
        return result;
    }

}
