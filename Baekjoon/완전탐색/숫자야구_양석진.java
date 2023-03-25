import com.sun.jdi.ArrayReference;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static ArrayList<BaseBallData> inputData = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int data = Integer.parseInt(st.nextToken());
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());

            BaseBallData baseBallData = new BaseBallData(data, strike, ball);
            inputData.add(baseBallData);
        }

        System.out.println(calcBaseBall());
    }

    static int calcBaseBall() {
        int result = 0;


        for (int i = 123; i <= 987; i++) {
            // 중복 숫자 체크
            if (!checksum(i)) continue; // 중복 숫자

            int allTestPass = 0;

            for (int j = 0; j < n; j++) {
                int strikeCount = 0;
                int ballCount = 0;

                // 이전에 입력 받은 클래스 객체 데이터
                BaseBallData current = inputData.get(j);

                // 사용할 데이터를 미리 변환
                String currentDataString = Integer.toString(current.data);

                // 완전 탐색을 시작할 데이터
                String searchDataString = Integer.toString(i);

                // 완전 탐색할 숫자와 입력 받은 데이터의 스트라이크 비교
                for (int k = 0; k < 3; k++) {
                    if (currentDataString.charAt(k) == searchDataString.charAt(k)) {
                        strikeCount++;
                    }
                }

                // 완전 탐색할 숫자와 입력 받은 데이터의 볼 비교
                for (int h = 0; h < 3; h++) {
                    for (int u = 0; u < 3; u++) {
                        if (searchDataString.charAt(h) == currentDataString.charAt(u)) {
                            // 볼은 위치가 다를 수 있기 때문에 한번 조건문을 넣어준 것
                            if (h != u) {
                                ballCount++;
                            }
                        }
                    }
                }
                if (current.strike == strikeCount && current.ball == ballCount) {
                    allTestPass++;
                }
            }
            if (allTestPass == n) {
                result++;
            }
        }
        return result;
    }

    static boolean checksum(int checkNum) {
        String numString = Integer.toString(checkNum);

        // 같으면 0을 리턴
        if (numString.charAt(0) == numString.charAt(1)) {
            return false;
        }
        if (numString.charAt(1) == numString.charAt(2)) {
            return false;
        }
        if (numString.charAt(0) == numString.charAt(2)) {
            return false;
        }
        if (numString.charAt(0) == '0' || numString.charAt(1) == '0' || numString.charAt(2) == '0') {
            return false;
        }
        return true;


    }

    static class BaseBallData {
        int data;
        int strike;
        int ball;

        public BaseBallData(int data, int strike, int ball) {
            this.data = data;
            this.strike = strike;
            this.ball = ball;
        }
    }
}