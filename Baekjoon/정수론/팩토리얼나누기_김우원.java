import java.util.Scanner;

public class 팩토리얼나누기_김우원 {//[15996] 팩토리얼 나누기

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        int ans = N / A;
        N /= A;
        while (N >= A) {
            ans += N / A;
            N /= A;
        }
        System.out.println(ans);
    }

}
