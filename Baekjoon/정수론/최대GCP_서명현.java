import java.io.*;
import java.util.*;

public class 최대GCD_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int repeatCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < repeatCount; i++) {
            List<Integer> arr = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int result = 0;
            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }
            for (int j = 0; j < arr.size(); j++) {
                for (int k = j + 1; k < arr.size(); k++) {
                    result = Math.max(result, gcd(arr.get(j), arr.get(k)));
                }
            }
            System.out.println(result);
        }
    }

    private static int gcd(int a, int b) { // 유클리드 호제법
        return b == 0 ? a : gcd(b, a % b);
    }
}
