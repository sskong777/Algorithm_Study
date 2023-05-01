import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	int N = Integer.parseInt(br.readLine());
	int[] stairs = new int[301];
	
	for(int i = 1; i < N+1; i++) {
		stairs[i] = Integer.parseInt(br.readLine());
	}
	int res = 0;
	int[] score = new int[301];
	score[1] = stairs[1];
	score[2] = stairs[1] + stairs[2];
	score[3] = Math.max(stairs[1], stairs[2]) + stairs[3];
	
	for (int n = 4; n <= N; n++) {
		score[n] = Math.max(score[n - 3] + stairs[n - 1], score[n - 2]) + stairs[n];
	}
	
	System.out.println(score[N]);
}	
	
}   