import java.io.*;

public class 청기백기_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int i = 1;
        while (Math.pow(i, 2) <= n) {
            i++;
        }
        System.out.println(--i);
    }
}
