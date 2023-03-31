import java.util.Scanner;

public class 청기백기_김우원 {//[15736] 청기 백기

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int ans = 0;
        for (int i = 1; i * i <= N; i++) ans++;
        System.out.println(ans);
    }

}
