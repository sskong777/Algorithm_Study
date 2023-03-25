package com.kosa.aps;

import java.io.*;
import java.util.*;

public class 일곱난쟁이_서명현 {

    static int N = 9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] heights = new int[N];
        int nonMemberIndex = 0;
        int nonMemberIndex2 = 0;
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            heights[i] = Integer.parseInt(br.readLine());
            sum += heights[i];
        }
        Arrays.sort(heights);
        for (int i = 0; i < heights.length - 1; i++) {
            for (int j = i + 1; j < heights.length; j++) {
                if (heights[i] + heights[j] == sum - 100) {
                    nonMemberIndex = i;
                    nonMemberIndex2 = j;
                    break;
                }
            }
        }
        for (int i = 0; i < heights.length; i++) {
            if (i == nonMemberIndex || i == nonMemberIndex2) {
                continue;
            }
            System.out.println(heights[i]);
        }
    }
}
