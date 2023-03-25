import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int check = 0;
        for (int a = 1; a <= N; a++) {
            for (int b = 1; b <= N; b++) {
                for (int c = 1; c <= N; c++) {
                    if(a+b+c == N){
                        if (c >= b + 2 && a % 2 == 0) check++;
                    }
                }
            }
        }
        System.out.println(check);
    }
}