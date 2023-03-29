import java.io.*;
import java.util.*;

public class 소수의자격_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int count = 0;

        for (int i = a; i <= b; i++) {
            if (containsD(i, d) && isPrimeNumber(i)) {
                count++;
            }
        }
        System.out.println(count);
    }

    private static boolean containsD(int target, int d) {
        return String.valueOf(target).contains(String.valueOf(d));
    }

    private static boolean isPrimeNumber(int num) {
        if (num == 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
