package com.kosa.aps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 완전제곱수_서명현 {

    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (j * j - i * i == n) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
