import java.io.*;

public class 뒤집어진소수_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long num = Long.parseLong(br.readLine());
        if (!isPrimeNumber(num) || !validate(num) || !isPrimeNumber(reverseNum)) {
            System.out.println("no");
            return;
        }
        System.out.println("yes");
    }

    private static long changeReverse(long num) {
        long result = 0;
        while (num > 0) {
            long target = num % 10;
            if (target == 6 || target == 9) {
                target = target == 6 ? 9 : 6;
            }
            result = result * 10 + target;
            num /= 10;
        }
        return result;
    }

    private static boolean validate(long num) {
        while (num > 0) {
            int target = (int) (num % 10);
            if (target == 3 || target == 4 || target == 7) {
                return false;
            }
            num /= 10;
        }
        return true;
    }

    private static boolean isPrimeNumber(long num) {
        if (num == 1) {
            return false;
        }
        for (long i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
