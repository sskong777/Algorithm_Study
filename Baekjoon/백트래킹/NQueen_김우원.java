import java.util.Scanner;

/*
[9663] N-Queen
 */
public class NQueen_김우원 {

    static int N;
    static int[] arr;
    static int ans;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N];
        backTrack(0);
        System.out.println(ans);
    }

    private static void backTrack(int cnt) {
        if (cnt == N) {
            ans++;
            return;
        }
        for (int i = 0; i < N; i++) {
            arr[cnt] = i;
            if (setQueen(cnt)) {
                backTrack(cnt + 1);
            }
        }
    }

    private static boolean setQueen(int col) {
        for (int i = 0; i < col; i++) {
            if (arr[col] == arr[i] || Math.abs(col - i) == Math.abs(arr[col] - arr[i]))
                return false;
        }
        return true;
    }

}
