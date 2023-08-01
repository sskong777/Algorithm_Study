import java.util.Scanner;

public class November_김우원 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a + b * 7 < 31) System.out.println(1);
        else System.out.println(0);
    }
}
