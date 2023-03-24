import java.io.IOException;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        int N = new Scanner(System.in).nextInt();
        boolean flag = true;

        // N이 0을 입력 받았을 떄
        if (N == 0) {
            flag = false;
        }
        while (N > 0) {
            // N을 3으로 나누었을 때, 나머지가 2가 나오면
            // 3으로 나누어 떨어지는 수가 하나도 없다는 뜻이다. 이는 3의 거듭제곱이 없다는 뜻
            // 왜 1이 아닌가? 3의 0제곱은 1이기 때문에 해결이 가능하다.
            if (N % 3 == 2) {
                flag = false;
                break;
            }
            N /= 3;
        }

        //
        System.out.println(flag ? "YES" : "NO");
    }
}