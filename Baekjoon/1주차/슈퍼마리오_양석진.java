import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] array = new int[10];

        for (int x = 0; x < 10; x++) {
            array[x] = Integer.parseInt(br.readLine());
        }

        int sum = 0;
        for (int x = 0; x < array.length; x++) {
            sum += array[x];

            if (Math.abs((sum - array[x]) - 100) < sum - 100) {
                sum = sum - array[x];
                break;
            }
        }
        System.out.println(sum);
    }
}