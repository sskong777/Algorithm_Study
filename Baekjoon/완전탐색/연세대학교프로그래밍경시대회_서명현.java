package com.kosa.aps;

import java.io.*;

public class 연세대학교프로그래밍경시대회_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int candyCount = Integer.parseInt(br.readLine());
        int result = 0;
        for (int t = 2; t < candyCount - 1; t += 2) {
            result += (candyCount - t - 2) / 2;
        }
        System.out.println(result);
    }
}
