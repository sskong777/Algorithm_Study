package com.kosa.aps;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 창고다각형_서명현 {

    static int[] storage;
    static int maxHeight;
    static int maxPosition;
    static int maxHeightCount;
    static int lastPosition;
    static int leftMaxHeight;
    static int leftMaxPosition;
    static int rightMaxHeight;
    static int rightMaxPosition;
    static int area;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        storage = new int[1001];
        maxHeight = 0;
        lastPosition = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int position = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            storage[position] = height;
            if (height > maxHeight) {
                maxHeight = height;
                maxPosition = position;
                maxHeightCount = 0;
            }
            if (height == maxHeight) {
                maxHeightCount++;
            }
            if (position > lastPosition) {
                lastPosition = position;
            }
        }

        //왼쪽
        leftMaxHeight = 0;
        leftMaxPosition = 0;
        area = 0;
        for (int i = 0; i < maxPosition; i++) {
            if (storage[i] > leftMaxHeight) {
                area += (i - leftMaxPosition) * leftMaxHeight;
                leftMaxHeight = storage[i];
                leftMaxPosition = i;
            }
        }
        area += (maxPosition - leftMaxPosition) * leftMaxHeight;

        // 오른쪽
        rightMaxHeight = 0;
        rightMaxPosition = 0;
        for (int i = lastPosition; i >= 0; i--) {
            if (storage[i] > rightMaxHeight) {
                area += (rightMaxPosition - i) * rightMaxHeight;
                rightMaxHeight = storage[i];
                rightMaxPosition = i;
            }
            if (storage[i] == maxHeight) {
                area += (i - maxPosition + 1) * maxHeight;
                break;
            }
        }
        System.out.println(area);
    }
}
