import java.util.Scanner;
public class 쉽게푸는문제_양석진 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int[] arr = new int[1002];

        int count = 1;
        for (int i = 1; i < 1000; i++) {
            for (int j = 0; j < i; j++) {
                if (count == 1001) break;
                arr[count] = i;
                count++;
            }
        }

        int sum = 0;

        for (int i = a; i <= b; i++) {
            sum += arr[i];
        }
        System.out.println(sum);
    }
}