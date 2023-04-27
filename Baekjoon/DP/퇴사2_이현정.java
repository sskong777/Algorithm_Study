import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;

	static int N, max;
	static int[] T, P, dp;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		T = new int[N+2];
		P = new int[N+2];
		dp = new int[N+2]; //dp[i] : i번째 전날까지의 최대 수익(i번째 날 상담 x)

		for (int i = 1; i <= N; ++i) {
			st = new StringTokenizer(br.readLine());
			int t = Integer.parseInt(st.nextToken());
			int p = Integer.parseInt(st.nextToken());

			T[i] = t;
			P[i] = p;
		}

		for (int i = 1; i <= N + 1; ++i) {
			//i번째 이전 까지의 최대 수익
			max = Math.max(max, dp[i]);

			//N + 1날에는 퇴사하기 때문에 x
			if (i + T[i] > N + 1) continue;

			//dp[i + T[i]] vs i 번째 날까지의 최대 수익(max) + i 번째 날의 상담 비용
			dp[i + T[i]] = Math.max(max + P[i], dp[i + T[i]]);
		}

		bw.write(max + "\n");
		bw.flush();bw.close();br.close();
	}
}