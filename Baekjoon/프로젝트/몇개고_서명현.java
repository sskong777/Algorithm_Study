import java.io.*;
import java.util.*;

public class 몇개고_서명현 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken()); // 시간
		int S = Integer.parseInt(st.nextToken()); // 술의 유무(0 : 술 X, 1 : 술 O)
		
		if(S == 1 || T <= 11 || T > 16) {
			System.out.println("280");
            return;
        }
		if(T >= 12 && T <= 16 && S == 0) {
			System.out.println("320");
		}
	}
}
