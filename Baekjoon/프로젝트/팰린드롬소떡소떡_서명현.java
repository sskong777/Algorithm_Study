import java.io.*;

public class 팰린드롬소떡소떡_서명현 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int cnt = 0;
        for (int i = 0; i < n/2; i++)
            if (s.charAt(i) != s.charAt(n-1-i))
                cnt++;
        System.out.println(cnt);
    }
}
