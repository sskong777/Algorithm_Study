
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[5];

        for (int x = 0; x < 5; x++) {
            arr[x] = Integer.parseInt(st.nextToken());
        }

        int count = 0;
        int n = 1;
        while (true) {
            for (int x = 0; x < arr.length; x++) {
                if (n % arr[x] == 0) {
                    count++;
                }
            }
            if (count >= 3) {
                System.out.println(n);
                break;
            } else {
                count = 0;
                n++;
            }
        }
    }
}