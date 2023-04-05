import java.util.Scanner;

public class 조합0의개수_김우원 {

    public static void main(String[] args) {//[2004] 조합 0의 개수
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int cnt2 = getCnt(N, 2) - getCnt(N - M, 2) - getCnt(M, 2);
        int cnt5 = getCnt(N, 5) - getCnt(N - M, 5) - getCnt(M, 5);
        System.out.println(Math.min(cnt2, cnt5));
    }

    private static int getCnt(int num, int div) {
        int cnt = 0;
        while (num >= div) {
            cnt += num / div;
            num /= div;
        }
        return cnt;
    }
}
