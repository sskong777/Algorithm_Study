import java.util.*;
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = 2 * sc.nextInt();
        int b = sc.nextInt();

        int discriminant = (int)Math.pow(a, 2) - (4 * b);
        int root1 = ((-1 * a) + (int)Math.sqrt(discriminant)) / 2;
        int root2 = ((-1 * a) - (int)Math.sqrt(discriminant)) / 2;

        if(root1 > root2){
            System.out.println(root2 + " " + root1);
        }else if(root1 == root2){
            System.out.println(root1);
        }else if(root1 < root2) {
            System.out.println(root1 + " " + root2);
        }
    }
}