import java.util.*;
import java.io.*;

public class 연세대학교프로그래밍경시대회_김우원 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int ans = 0;
		for(int 택희 = 2; 택희 < N; 택희+=2) {
			for(int 영훈 = 1; 영훈 < N; 영훈++) {
				int 남규 = N - 택희 - 영훈;
				if(남규 >= 영훈 + 2) ans++;
			}
		}
		System.out.println(ans);
	}
	
}
