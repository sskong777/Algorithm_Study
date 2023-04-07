import java.util.*;
import java.io.*;

public class 고냥이_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();

        int[] alphabet = new int[26];
        int start = 0;
        int end = 0;
        int count = 0;
        int result = 0;

        while (end < str.length()) {
            int num = str.charAt(end) - 'a';
            alphabet[num]++;
            if (alphabet[num] == 1) count++;

            while (count > N) {
                int num2 = str.charAt(start) - 'a';
                alphabet[num2]--;
                if (alphabet[num2] == 0) count--;
                start++;
            }
            result = Math.max(result, end - start + 1);
            end++;
        }
        System.out.println(result);
    }
}