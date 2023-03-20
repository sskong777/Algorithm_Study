package com.kosa.aps;

import java.io.*;
import java.util.*;

public class 대회or인턴_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int team = 0;
        if (n + m > k) {
            team = Math.min(n / 2, m);
            k -= (n + m) - team * 3;
            if (k > 0) {
                team -= (k + 2) / 3;
            }
        }
        System.out.println(team);
    }
}
