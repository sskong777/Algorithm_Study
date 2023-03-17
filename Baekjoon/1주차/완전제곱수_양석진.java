import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        ArrayList<Integer> arrayList = new ArrayList<>();

        for (int a = 1; a <= 500; a++) {
            for (int b = 1; b <= 500; b++) {
                if ((Math.pow(a, 2) == Math.pow(b, 2) - n)) {
                    arrayList.add(a);
                    arrayList.add(b);
                    break;
                }
            }
        }

        bw.write(String.valueOf(arrayList.size() / 2));
        bw.close();
    }
}