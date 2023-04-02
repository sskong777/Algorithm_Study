import java.io.*;
import java.util.*;

public class 팩토리얼나누기_양석진 {
    public static void main(String[] args) throws IOException {

        // 우원님 풀이 참고했습니다..
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int ans = N / A;
        N /= A;
        while (N >= A) {
            ans += N / A;
            N /= A;
        }
        System.out.println(ans);
    }
}
