import java.util.Scanner;

public class 큐브더미_박주원 {

	static final int MAX = 5;
	static boolean[][][] Cube = new boolean[MAX][MAX][MAX];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		for (int i = 0; i < M; i++) {
			int X = sc.nextInt();
			int Y = sc.nextInt();
			int Z = sc.nextInt();
			Cube[X][Y][Z] = true;
		}

		int Answer = 0;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				for (int k = 1; k <= N; k++) {
					if (Cube[i][j][k]) {
						if (Cube[i + 1][j][k] && Cube[i - 1][j][k] && Cube[i][j + 1][k] && Cube[i][j - 1][k]
								&& Cube[i][j][k + 1] && Cube[i][j][k - 1]) {
							Answer++;
						}
					}
				}
			}
		}

		System.out.println(Answer);

	}

}
