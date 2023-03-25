package com.kosa.aps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 왼전제곱수_김우원 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int ans = 0;
		for (int B = 1; B < 501; B++) {
			int powB = (int) Math.pow(B, 2);
			for (int A = B; A < 501; A++) {
				int powA = (int) Math.pow(A, 2);
				if (powA == powB + N) ans++;
			}
		}
		System.out.println(ans);
	}

}
