import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int result = 0;

        for(int x = 0; x<=300; x++){
            for(int y = 0; y<=300; y++){
                for(int z = 0; z<=300; z++){
                    if(x * A + y * B + C * z == N){
                        result = 1;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
