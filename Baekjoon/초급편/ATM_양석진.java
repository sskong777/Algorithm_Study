import java.util.Scanner;
import java.util.Arrays;

public class ATM_양석진 {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }

        Arrays.sort(arr);

        int before = 0;
        int sum = 0;

        for(int i = 0; i < N; i++) {
            sum += before + arr[i];

            before += arr[i];
        }
        System.out.println(sum);
    }
}