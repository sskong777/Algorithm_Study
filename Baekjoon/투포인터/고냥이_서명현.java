import java.io.*;

public class 고냥이_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int left = 0;
        int right = 0;
        int max = 0;
        int[] check = new int[26];
        int count = 0;
        while (right < s.length()) {
            int num = s.charAt(right) - 'a';
            check[num]++;
            if (check[num] == 1) {
                count++;
            }
            while(count > n) {
                int num2 = s.charAt(left) - 'a';
                check[num2]--;
                if (check[num2] == 0) {
                    count--;
                }
                left++;
            }
            max = Math.max(max, right - left + 1);
            right++;
        }
        System.out.println(max);
    }
}
