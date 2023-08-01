import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 첨탑밀어서부수기_김우원 {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int curr = Integer.parseInt(stk.nextToken());
        int ans = 1;
        for(int i = 1; i < N; i++) {
            int next =  Integer.parseInt(stk.nextToken());
            if(curr <= next) ans++;
            curr = next;
        }
        System.out.println(ans);
    }
}
