import java.io.*;
import java.util.*;

public class ThreeDots_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int a[] = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) a[i] = Integer.parseInt(st.nextToken());

            int cnt = 0;
            Arrays.sort(a);
            for (int i = 0; i < N - 2; i++) {
                int k = i + 2;
                for (int j = i + 1; j < N - 1; j++) {
                    int ba = a[j] - a[i];

                    while (k < N && a[k] - a[j] < ba) {
                        k++;
                    }

                    if (k == N) break;
                    if (a[k] - a[j] == ba) cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
}