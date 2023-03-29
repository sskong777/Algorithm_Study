import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int x = 0; x < N; x++) {
            ArrayList<Integer> inputList = new ArrayList<Integer>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int answer = 0;
            while (st.hasMoreTokens()) {
                inputList.add(Integer.parseInt(st.nextToken()));
            }
            // 최대 공약수 구하기
            for (int y = 0; y < inputList.size(); y++) {
                for (int z = y + 1; z < inputList.size(); z++) {
                    answer = Math.max(answer, GCD(inputList.get(y), inputList.get(z)));
                }
            }
            System.out.println(answer);
        }
    }

    // 유클리드 호제법 - 재귀함수 사용, 반복문 사용 시, 시간초과
    public static int GCD(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return GCD(b, a % b);
        }
    }
}