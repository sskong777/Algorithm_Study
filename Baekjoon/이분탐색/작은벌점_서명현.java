import java.io.*;
import java.util.*;

public class 작은벌점_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] aArr = new int[a];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < a; i++) {
            aArr[i] = Integer.parseInt(st.nextToken());
        }
        int[] bArr = new int[b];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < b; i++) {
            bArr[i] = Integer.parseInt(st.nextToken());
        }
        int[] cArr = new int[c];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < c; i++) {
            cArr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(aArr);
        Arrays.sort(bArr);
        Arrays.sort(cArr);

        int result = Integer.MAX_VALUE;
        for (int selectA : aArr) {
            // 1. selectA와 가까운 selectB를 선택, selectA와 selectB 중 각각 가까운 selectC 선택
            int selectB = findNearestValue(bArr, selectA);
            int selectC1 = findNearestValue(cArr, selectA);
            int selectC2 = findNearestValue(cArr, selectB);

            // 2-1. selectA와 가까운 selectC1일 경우의 score 계산
            int score1 = calculateScore(selectA, selectB, selectC1);

            // 2-1. selectA와 가까운 selectC2일 경우의 score 계산
            int score2 = calculateScore(selectA, selectB, selectC2);

            // 3. selectC1, selectC2 둘 중 차이가 적은 result 갱신
            result = Math.min(result, Math.min(score1, score2));
        }
        System.out.println(result);
    }

    private static int findNearestValue(int[] arr, int val) {
        int start = 0;
        int end = arr.length - 1;
        int mid = (start + end) / 2;
        int nearest = arr[mid];

        while (start <= end) {
            mid = (start + end) / 2;
            if (arr[mid] == val) {
                return val;
            } else if (arr[mid] < val) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
            nearest = getClosestTo(arr[mid], nearest, val);
        }
        return nearest;
    }

    private static int calculateScore(int score1, int score2, int score3) {
        int max = Math.max(Math.max(score1, score2), score3);
        int min = Math.min(Math.min(score1, score2), score3);
        return max - min;
    }

    private static int getClosestTo(int a, int b, int val) {
        return (Math.abs(a - val) < Math.abs(b - val)) ? a : b;
    }
}
