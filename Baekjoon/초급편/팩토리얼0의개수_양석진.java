import java.util.Scanner;

public class 팩토리얼0의개수_양석진 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int num = in.nextInt();
        int count = 0;

        while (num >= 5) {
            count += num / 5;
            num /= 5;
        }
        System.out.println(count);
    }
<<<<<<< HEAD
=======

>>>>>>> 3a969475d5c2d059b7a5d8aba7ffb47101a3394e
}