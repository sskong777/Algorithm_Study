package com.kosa.aps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 통학의신_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int a = Integer.parseInt(s[0]);
        int b = Integer.parseInt(s[1]);
        int d = a * a - b;
        if (d == 0) {
            System.out.println(-a);
            return;
        }
        System.out.println((int) (-Math.sqrt(d) - a) + " " + (int) (Math.sqrt(d) - a));
    }
}
