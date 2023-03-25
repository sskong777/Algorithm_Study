package com.kosa.aps;

import java.io.*;
import java.util.*;

public class Farm_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int totalNum = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int count = 0;
        int sheep = 0;
        for (int i = 1; i < totalNum; i++) {
            if (i * a + (totalNum - i) * b == w) {
                count++;
                sheep = i;
            }
        }
        if (count == 1) {
            System.out.println(sheep + " " + (totalNum - sheep));
            return;
        }
        System.out.println(-1);
    }
}
