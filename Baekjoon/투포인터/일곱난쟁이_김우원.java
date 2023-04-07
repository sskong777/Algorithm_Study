import java.util.Arrays;
import java.util.Scanner;

/*
[2309] 일곱 난쟁이
 */
public class 일곱난쟁이_김우원 {
    static int[] sel = new int[7];
    static int[] arr = new int[9];
    static StringBuilder sb;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 9; i++) arr[i] = sc.nextInt();
        Arrays.sort(arr);
        combination(0,0);
        System.out.println(sb);
    }

    static void combination(int st, int depth) {
        if (depth == 7) {
            int temp = 0;
            for(int i : sel) temp += arr[i];
            if(temp == 100) {
                sb = new StringBuilder();
                for(int i : sel) sb.append(arr[i]).append("\n");
            }
            return;
        }

        for (int i = st; i < 9; i++) {
            sel[depth] = i;
            combination(i + 1, depth + 1);
        }

    }
}
