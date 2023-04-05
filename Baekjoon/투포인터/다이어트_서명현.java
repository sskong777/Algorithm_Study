import java.util.*;

public class 다이어트_서명현 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int g = scanner.nextInt();

        long left = 1;
        long right = 2;
        boolean hasResult = false;
        while (right < 100000) {
            long diff = right * right - left * left;
            if (diff == g) {
                System.out.println(right);
                hasResult = true;
            }
            if (diff > g) {
                left++;
                continue;
            }
            right++;
        }
        if (!hasResult) {
            System.out.println(-1);
        }
    }
}
