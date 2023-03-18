package com.kosa.aps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 슈퍼마리오_서명현 {

    static int INPUT_COUNT = 10;
    static int TOTAL = 100;
    static int max;
    static int sum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[INPUT_COUNT];
        for (int i = 0; i < INPUT_COUNT; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        sum = 0;
        for (int i = 0; i < INPUT_COUNT; i++) {
            sum += arr[i];
            if (sum >= 100) {
                max = i;
                break;
            }
        }
        if (sum - TOTAL <= TOTAL - sum + arr[max]) {
            System.out.println(sum);
            return;
        }
        System.out.println(sum - arr[max]);
    }
}
