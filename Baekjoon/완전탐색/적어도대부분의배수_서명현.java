package com.kosa.aps;

import java.io.*;
import java.util.*;

public class 적어도대부분의배수_서명현 {

    static final int num = 5;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[num];
        for (int i = 0; i < num; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int value = 1;
        int count = 0;
        while (true) {
            for (int a : arr) {
                if (value % a == 0) {
                    count++;
                }
            }
            if (count >= 3) {
                System.out.println(value);
                break;
            }
            count = 0;
            value++;
        }
    }
}
