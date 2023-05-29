import java.util.Scanner;

public class 몇개고_김우원 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int s = sc.nextInt();
        System.out.println(t >= 12 && t <= 16 && s == 0 ? 320 : 280);
    }
}
