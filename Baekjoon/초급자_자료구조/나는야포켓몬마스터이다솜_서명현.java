import java.io.*;
import java.util.*;

public class 나는야포켓몬마스터이다솜_서명현 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String[] names = new String[n + 1];
        Map<String, Integer> hashMap = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            names[i] = br.readLine();
            hashMap.put(names[i], i);
        }
        for (int i = 0; i < m; i++) {
            String s = br.readLine();
            if (isNumber(s)) {
                int i1 = Integer.parseInt(s);
                System.out.println(names[i1]);
                continue;
            }
            System.out.println(hashMap.get(s));
        }
    }

    private static boolean isNumber(String s) {
        try {
            Integer.parseInt(s);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }
}
